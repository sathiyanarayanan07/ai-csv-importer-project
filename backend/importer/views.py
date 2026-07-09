from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Upload,CRMLead
from .serializers import UploadSerializer , CRMLeadSerializer
from .services.csv_services import read_csv
from rest_framework.views import APIView
from .services.ai_service import process

import logging

logger = logging.getLogger(__name__)

# Create your views here.



class UploadcsvView(APIView):
    def post(self, request):
        
        serializer = UploadSerializer(data = request.data)
        
        if not serializer.is_valid():
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        upload = serializer.save()
        
        try:
            csv_data = read_csv(upload.file.path)
            
            return Response({
                    "success" : True,
                    "upload_id":upload.id,
                    "file_name":upload.file.name,
                    "columns": csv_data["columns"],
                    "total_rows": csv_data["total_rows"],
                    "preview": csv_data["preview"]
                })
        except Exception as e:
            
            upload.delete()
            
            return Response(
                 {
                   "success": False,
                   "error": str(e)
        },
        status=status.HTTP_400_BAD_REQUEST
    )

class ImportCsvview(APIView):

    def post(self, request):

        upload_id = request.data.get("upload_id")

        if not upload_id:
            return Response(
                {"error": "upload_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            upload = Upload.objects.get(id=upload_id)

        except Upload.DoesNotExist:
            return Response(
                {"error": "Upload not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        csv_data = read_csv(upload.file.path)
        rows = csv_data["records"]

        batch_size = 20

        imported = []
        skipped = []

        for i in range(0, len(rows), batch_size):

            batch = rows[i:i + batch_size]

            try:
                ai_records = process(batch)

                print("AI Records:")
                print(ai_records)

                for lead in ai_records:

                    lead["upload"] = upload.id

                    serializer = CRMLeadSerializer(data=lead)

                    if serializer.is_valid():

                        serializer.save()
                        imported.append(serializer.data)

                    else:

                        print("\nValidation Error")
                        print("Lead:", lead)
                        print("Errors:", serializer.errors)

                        skipped.append({
                            "record": lead,
                            "errors": serializer.errors
                        })

            except Exception as e:
                logger.exception("Gemini batch processing failed")
                skipped.extend(batch)

        return Response({
            "success": True,
            "total_rows": len(rows),
            "imported": len(imported),
            "skipped": len(skipped),
            "records": imported,
            "skipped_records": skipped
        })
    
class CRMLeadListView(ListAPIView):
    queryset = CRMLead.objects.all().order_by("-imported_at")
    serializer_class = CRMLeadSerializer