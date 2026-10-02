train_data = [
    {
        "text": """
            Invoice No: INV-1001
            Vendor: Acme Pte Ltd
            Total: SGD 1,250.00
            Date: 2026-09-15
            """,
        "expected": {
            "vendor": "Acme Pte Ltd",
            "invoice_number": "INV-1001",
            "total": 1250.00,
            "currency": "SGD"
        }
    },

    {
        "text": """
            Invoice #: ABC-8821
            Supplier: Global Tech Solutions
            Amount Due: USD 842.50
            Invoice Date: 2026-09-20
            """,
        "expected": {
            "vendor": "Global Tech Solutions",
            "invoice_number": "ABC-8821",
            "total": 842.50,
            "currency": "USD"
        }
    },

    {
        "text": """
            Bill Number: SG-5542
            Company: Singapore Office Supplies
            Grand Total: SGD 320.80
            Date Issued: 2026-09-22
            """,
        "expected": {
            "vendor": "Singapore Office Supplies",
            "invoice_number": "SG-5542",
            "total": 320.80,
            "currency": "SGD"
        }
    }
]


test_data = [
    {
        "text": """
            Invoice ID: XZ-7712
            Issued by: Pacific Logistics Pte Ltd
            Amount: SGD 2,450.00
            Issued: 2026-09-28
            """,
        "expected": {
            "vendor": "Pacific Logistics Pte Ltd",
            "invoice_number": "XZ-7712",
            "total": 2450.00,
            "currency": "SGD"
        }
    },

    {
        "text": """
            Invoice Number: US-19382
            From: Data Systems Inc.
            Total Amount: USD 1,099.99
            Invoice Date: 2026-09-29
            """,
        "expected": {
            "vendor": "Data Systems Inc.",
            "invoice_number": "US-19382",
            "total": 1099.99,
            "currency": "USD"
        }
    }
]