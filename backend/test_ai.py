from backend.importer.services.ai_service import process

rows = [
    {
        "Customer Name": "John Doe",
        "Primary Email": "john@gmail.com",
        "Phone Number": "9876543210",
        "City": "Mumbai",
        "Remark": "Interested"
    }
]

print(process(rows))