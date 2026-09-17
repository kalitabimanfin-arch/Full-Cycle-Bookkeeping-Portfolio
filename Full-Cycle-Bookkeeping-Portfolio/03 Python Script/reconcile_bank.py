import csv

# =============================================
# AUTOMATED BANK RECONCILIATION
# Bluepeak Creative Studio LLC - Q1 2026
# =============================================

# Load bank statement
with open("bank_statement_q1_2026.csv", "r", encoding="utf-8") as f:
    bank = list(csv.DictReader(f))

# Load QBO transactions
with open("qbo_transactions_all.csv", "r", encoding="utf-8") as f:
    txns = list(csv.DictReader(f))

# Filter for bank transactions only
bank_txns = [t for t in txns if t["Account"] == "Business Checking - Chase"]

# Build bank statement lines (skip opening balance)
bank_lines = []
for row in bank:
    if row["Description"] == "Opening Balance":
        continue
    amount = float(row["Debit"]) if row["Debit"] else -float(row["Credit"])
    bank_lines.append({
        "date": row["Date"],
        "description": row["Description"],
        "amount": abs(amount)
    })

# Build QBO transaction list
qbo_list = []
for t in bank_txns:
    qbo_list.append({
        "date": t["Date"],
        "description": t["Description"],
        "amount": abs(float(t["Amount"]))
    })

# Find matches and discrepancies
matched = []
unmatched_in_bank = []
unmatched_in_qbo = qbo_list.copy()

for bank_item in bank_lines:
    bank_amt = bank_item["amount"]
    found = False
    for qbo_item in unmatched_in_qbo:
        if abs(bank_amt - qbo_item["amount"]) < 0.01:
            matched.append(bank_item)
            unmatched_in_qbo.remove(qbo_item)
            found = True
            break
    if not found:
        unmatched_in_bank.append(bank_item)

# =============================================
# REPORT
# =============================================
print("=" * 60)
print("BANK RECONCILIATION REPORT")
print("Bluepeak Creative Studio LLC - Q1 2026")
print("=" * 60)

print(f"\n✅ MATCHED TRANSACTIONS: {len(matched)}")

print(f"\n⚠️  IN BANK BUT NOT IN QBO (needs adjustment): {len(unmatched_in_bank)}")
for item in unmatched_in_bank:
    print(f"   - {item['description']}: ${item['amount']:.2f}")

print(f"\n⚠️  IN QBO BUT NOT CLEARED BY BANK (outstanding): {len(unmatched_in_qbo)}")
for item in unmatched_in_qbo:
    print(f"   - {item['description']}: ${item['amount']:.2f}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"Total bank statement lines: {len(bank_lines)}")
print(f"Total QBO transactions: {len(bank_txns)}")
print(f"Matched: {len(matched)}")
print(f"Discrepancies found: {len(unmatched_in_bank) + len(unmatched_in_qbo)}")