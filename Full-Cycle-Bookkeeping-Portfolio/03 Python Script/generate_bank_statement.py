import csv
from datetime import datetime

# =============================================
# MOCK BANK STATEMENT GENERATOR
# Bluepeak Creative Studio LLC - Q1 2026
# =============================================

# Read the generated transactions
with open("qbo_transactions_all.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    all_txns = list(reader)

# Only keep transactions that hit the bank account
bank_txns = [t for t in all_txns if t["Account"] == "Business Checking - Chase"]

# Sort by date
bank_txns.sort(key=lambda x: x["Date"])

# Start with initial balance
balance = 0.0
statement_rows = []

# Add opening balance line
statement_rows.append({
    "Date": "2026-01-01",
    "Description": "Opening Balance",
    "Debit": "",
    "Credit": "",
    "Balance": 0.00
})

# Add each bank transaction
for txn in bank_txns:
    amount = float(txn["Amount"])
    balance += amount

    debit = abs(amount) if amount < 0 else ""
    credit = amount if amount > 0 else ""

    statement_rows.append({
        "Date": txn["Date"],
        "Description": txn["Description"],
        "Debit": debit,
        "Credit": credit,
        "Balance": round(balance, 2)
    })

# =============================================
# INJECT 3 INTENTIONAL DISCREPANCIES
# =============================================

# Discrepancy 1: Bank fee not in QBO
statement_rows.append({
    "Date": "2026-01-31",
    "Description": "WIRE TRANSFER FEE - NOT IN QBO",
    "Debit": 20.00,
    "Credit": "",
    "Balance": round(balance - 20.00, 2)
})
balance -= 20.00

# Discrepancy 2: Outstanding check
statement_rows.append({
    "Date": "2026-03-28",
    "Description": "OUTSTANDING CHECK #1001 - OFFICE SUPPLIES",
    "Debit": 250.00,
    "Credit": "",
    "Balance": round(balance - 250.00, 2)
})
balance -= 250.00

# Discrepancy 3: Interest earned
statement_rows.append({
    "Date": "2026-03-31",
    "Description": "INTEREST EARNED - NOT IN QBO",
    "Debit": "",
    "Credit": 12.50,
    "Balance": round(balance + 12.50, 2)
})
balance += 12.50

# Sort by date again
statement_rows.sort(key=lambda x: x["Date"])

# Save to CSV
with open("bank_statement_q1_2026.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Description", "Debit", "Credit", "Balance"])
    writer.writeheader()
    writer.writerows(statement_rows)

print(f"✅ Bank statement generated!")
print(f"📁 Saved to: bank_statement_q1_2026.csv")
print(f"📊 Total rows: {len(statement_rows)}")
print(f"💰 Final Balance: ${balance:,.2f}")
print()
print("🚨 3 INTENTIONAL DISCREPANCIES ADDED:")
print("   1. Wire transfer fee ($20) - in bank, not in QBO")
print("   2. Outstanding check #1001 ($250) - in QBO, not cleared by bank")
print("   3. Interest earned ($12.50) - in bank, not in QBO")