import csv
import random
from datetime import datetime, timedelta

# =============================================
# BLUEPEAK CREATIVE STUDIO LLC
# Transaction Generator (Jan-Mar 2026)
# =============================================

random.seed(42)  # Reproducible results

clients = [
    "Lone Star Coffee Co.", "Cedar Creek Realty", "Austin Wellness Spa",
    "Texas Trail Outfitters", "Hill Country Winery", "Bright Path Academy",
    "Rio Grande Tacos", "Lone Star Tech Solutions"
]

services = [
    ("Design Services Revenue", 800, 2500),
    ("Branding Package Revenue", 1500, 3500),
    ("Consulting Revenue", 500, 1500),
]

all_transactions = []

# =============================================
# JANUARY 2026 (STARTUP MONTH)
# =============================================
jan_start = datetime(2026, 1, 1)

# Owner contributions
all_transactions.append({
    "Date": "2026-01-02", "Type": "Owner Contribution",
    "Description": "Member A capital contribution", "Account": "Business Checking - Chase",
    "Amount": 15000.00, "Category": "Owner's Capital - Member A"
})
all_transactions.append({
    "Date": "2026-01-02", "Type": "Owner Contribution",
    "Description": "Member B capital contribution", "Account": "Business Checking - Chase",
    "Amount": 15000.00, "Category": "Owner's Capital - Member B"
})

# Equipment purchase
all_transactions.append({
    "Date": "2026-01-05", "Type": "Expense",
    "Description": "MacBooks and studio equipment", "Account": "Business Checking - Chase",
    "Amount": -8500.00, "Category": "Office Equipment"
})

# January sales invoices (12)
for i in range(12):
    client = random.choice(clients)
    service, low, high = random.choice(services)
    amount = round(random.uniform(low, high), 2)
    day = random.randint(5, 28)
    date = datetime(2026, 1, day).strftime("%Y-%m-%d")
    all_transactions.append({
        "Date": date, "Type": "Sales Invoice",
        "Description": f"Invoice to {client} - {service}", "Account": "Accounts Receivable",
        "Amount": amount, "Category": service
    })

# January expense bills (8)
expenses_jan = [
    ("Adobe Creative Cloud subscription", -59.99, "Software Subscriptions"),
    ("Studio rent - January", -1500.00, "Rent Expense"),
    ("Office supplies - Staples", -145.20, "Office Supplies"),
    ("Google Ads campaign", -350.00, "Marketing & Advertising"),
    ("Business insurance premium", -300.00, "Insurance Expense"),
    ("Legal consultation", -400.00, "Professional Fees"),
    ("Canva Pro subscription", -14.99, "Software Subscriptions"),
    ("Figma subscription", -15.00, "Software Subscriptions"),
]
for desc, amount, category in expenses_jan:
    day = random.randint(3, 28)
    all_transactions.append({
        "Date": f"2026-01-{day:02d}", "Type": "Expense Bill",
        "Description": desc, "Account": "Accounts Payable",
        "Amount": amount, "Category": category
    })

# January payroll
all_transactions.append({
    "Date": "2026-01-31", "Type": "Payroll",
    "Description": "January payroll - part-time employee", "Account": "Business Checking - Chase",
    "Amount": -1800.00, "Category": "Salaries & Wages"
})
all_transactions.append({
    "Date": "2026-01-31", "Type": "Payroll Tax",
    "Description": "Employer payroll taxes - January", "Account": "Business Checking - Chase",
    "Amount": -180.00, "Category": "Payroll Taxes"
})

# January bank fee
all_transactions.append({
    "Date": "2026-01-31", "Type": "Bank Fee",
    "Description": "Chase monthly service fee", "Account": "Business Checking - Chase",
    "Amount": -15.00, "Category": "Bank Fees"
})

# January owner draws
all_transactions.append({
    "Date": "2026-01-15", "Type": "Owner Draw",
    "Description": "Member A draw - January", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member A"
})
all_transactions.append({
    "Date": "2026-01-15", "Type": "Owner Draw",
    "Description": "Member B draw - January", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member B"
})

# =============================================
# FEBRUARY 2026 (FULL OPERATIONS)
# =============================================

# February sales invoices (14)
for i in range(14):
    client = random.choice(clients)
    service, low, high = random.choice(services)
    amount = round(random.uniform(low, high), 2)
    day = random.randint(1, 28)
    date = datetime(2026, 2, day).strftime("%Y-%m-%d")
    all_transactions.append({
        "Date": date, "Type": "Sales Invoice",
        "Description": f"Invoice to {client} - {service}", "Account": "Accounts Receivable",
        "Amount": amount, "Category": service
    })

# February expense bills (8)
expenses_feb = [
    ("Adobe Creative Cloud subscription", -59.99, "Software Subscriptions"),
    ("Studio rent - February", -1500.00, "Rent Expense"),
    ("Client lunch meeting - Rio Grande Tacos", -85.50, "Marketing & Advertising"),
    ("Facebook Ads campaign", -275.00, "Marketing & Advertising"),
    ("New office chair - Herman Miller", -650.00, "Office Supplies"),
    ("Sketch subscription", -9.00, "Software Subscriptions"),
    ("Print materials - business cards", -120.00, "Marketing & Advertising"),
    ("Website hosting - Squarespace", -16.00, "Software Subscriptions"),
]
for desc, amount, category in expenses_feb:
    day = random.randint(1, 28)
    all_transactions.append({
        "Date": f"2026-02-{day:02d}", "Type": "Expense Bill",
        "Description": desc, "Account": "Accounts Payable",
        "Amount": amount, "Category": category
    })

# February payroll
all_transactions.append({
    "Date": "2026-02-28", "Type": "Payroll",
    "Description": "February payroll - part-time employee", "Account": "Business Checking - Chase",
    "Amount": -1800.00, "Category": "Salaries & Wages"
})
all_transactions.append({
    "Date": "2026-02-28", "Type": "Payroll Tax",
    "Description": "Employer payroll taxes - February", "Account": "Business Checking - Chase",
    "Amount": -180.00, "Category": "Payroll Taxes"
})

# February bank fee
all_transactions.append({
    "Date": "2026-02-28", "Type": "Bank Fee",
    "Description": "Chase monthly service fee", "Account": "Business Checking - Chase",
    "Amount": -15.00, "Category": "Bank Fees"
})

# February refund (discount)
all_transactions.append({
    "Date": "2026-02-18", "Type": "Refund",
    "Description": "Client refund - duplicate billing", "Account": "Business Checking - Chase",
    "Amount": -400.00, "Category": "Discounts & Refunds"
})

# February owner draws
all_transactions.append({
    "Date": "2026-02-15", "Type": "Owner Draw",
    "Description": "Member A draw - February", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member A"
})
all_transactions.append({
    "Date": "2026-02-15", "Type": "Owner Draw",
    "Description": "Member B draw - February", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member B"
})

# =============================================
# MARCH 2026 (QUARTER-END)
# =============================================

# March sales invoices (16)
for i in range(16):
    client = random.choice(clients)
    service, low, high = random.choice(services)
    amount = round(random.uniform(low, high), 2)
    day = random.randint(1, 30)
    date = datetime(2026, 3, day).strftime("%Y-%m-%d")
    all_transactions.append({
        "Date": date, "Type": "Sales Invoice",
        "Description": f"Invoice to {client} - {service}", "Account": "Accounts Receivable",
        "Amount": amount, "Category": service
    })

# March expense bills (9)
expenses_mar = [
    ("Adobe Creative Cloud subscription", -59.99, "Software Subscriptions"),
    ("Studio rent - March", -1500.00, "Rent Expense"),
    ("Google Ads campaign - Q1 push", -500.00, "Marketing & Advertising"),
    ("Quarterly software renewal - Adobe", -600.00, "Software Subscriptions"),
    ("Networking event - Austin Chamber", -200.00, "Marketing & Advertising"),
    ("New printer - HP", -350.00, "Office Supplies"),
    ("Webflow annual plan", -276.00, "Software Subscriptions"),
    ("Client gifts - holiday packages", -180.00, "Marketing & Advertising"),
    ("AWS hosting renewal", -120.00, "Software Subscriptions"),
]
for desc, amount, category in expenses_mar:
    day = random.randint(1, 30)
    all_transactions.append({
        "Date": f"2026-03-{day:02d}", "Type": "Expense Bill",
        "Description": desc, "Account": "Accounts Payable",
        "Amount": amount, "Category": category
    })

# March payroll
all_transactions.append({
    "Date": "2026-03-31", "Type": "Payroll",
    "Description": "March payroll - part-time employee", "Account": "Business Checking - Chase",
    "Amount": -1800.00, "Category": "Salaries & Wages"
})
all_transactions.append({
    "Date": "2026-03-31", "Type": "Payroll Tax",
    "Description": "Employer payroll taxes - March", "Account": "Business Checking - Chase",
    "Amount": -180.00, "Category": "Payroll Taxes"
})

# March bank fee
all_transactions.append({
    "Date": "2026-03-31", "Type": "Bank Fee",
    "Description": "Chase monthly service fee", "Account": "Business Checking - Chase",
    "Amount": -15.00, "Category": "Bank Fees"
})

# March insurance prepayment
all_transactions.append({
    "Date": "2026-03-05", "Type": "Prepaid Expense",
    "Description": "Annual business insurance prepayment", "Account": "Business Checking - Chase",
    "Amount": -3600.00, "Category": "Prepaid Insurance"
})

# March deferred revenue (client prepayment)
all_transactions.append({
    "Date": "2026-03-22", "Type": "Deferred Revenue",
    "Description": "Client prepayment for April project - Hill Country Winery", "Account": "Business Checking - Chase",
    "Amount": 5000.00, "Category": "Deferred Revenue"
})

# March owner draws
all_transactions.append({
    "Date": "2026-03-15", "Type": "Owner Draw",
    "Description": "Member A draw - March", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member A"
})
all_transactions.append({
    "Date": "2026-03-15", "Type": "Owner Draw",
    "Description": "Member B draw - March", "Account": "Business Checking - Chase",
    "Amount": -2000.00, "Category": "Owner's Draw - Member B"
})

# =============================================
# SORT AND SAVE
# =============================================

all_transactions.sort(key=lambda x: x["Date"])

with open("transactions.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Type", "Description", "Account", "Amount", "Category"])
    writer.writeheader()
    writer.writerows(all_transactions)

print(f"✅ Generated {len(all_transactions)} transactions!")
print(f"📁 Saved to: transactions.csv")
print(f"📅 Period: Jan 1 - Mar 31, 2026")
print(f"📊 Total transactions: {len(all_transactions)}")
print("\n📋 Breakdown by type:")
types = {}
for t in all_transactions:
    types[t["Type"]] = types.get(t["Type"], 0) + 1
for t, count in sorted(types.items()):
    print(f"   {t}: {count}")