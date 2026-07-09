from django.urls import path
from .views import UploadcsvView , ImportCsvview,CRMLeadListView

urlpatterns = [

    path("upload/", UploadcsvView.as_view(), name="upload_csv" ),
    path("import/", ImportCsvview.as_view(), name="importdata"),
     path("leads/", CRMLeadListView.as_view(), name="lead"),


]