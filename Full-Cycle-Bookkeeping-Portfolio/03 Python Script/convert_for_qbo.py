import csv

# Read the original bank statement
with open("bank_statement_q1_2026.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

# Convert to QBO-friendly format with CONSISTENT dates
output = []
for row in rows:
    # Skip opening balance
    if row["Description"] == "Opening Balance":
        continue

    # Parse date from DD-MM-YYYY format
    date_str = row["Date"].strip()
    parts = date_str.split("-")
    
    if len(parts) == 3:
        day, month, year = parts
        formatted_date = f"{month}/{day}/{year}"  # Force MM/DD/YYYY
    else:
        formatted_date = date_str

    # Convert Debit/Credit to single Amount
    if row["Debit"]:
        amount = -float(row["Debit"])
    elif row["Credit"]:
        amount = float(row["Credit"])
    else:
        continue

    output.append({
        "Date": formatted_date,
        "Description": row["Description"],
        "Amount": amount
    })

# Save to NEW filename (avoids lock issues)
with open("qbo_import_final.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Date", "Description", "Amount"])
    writer.writeheader()
    writer.writerows(output)

print(f"✅ Converted {len(output)} transactions!")
print(f"📁 Saved to: qbo_import_final.csv")
print(f"\n📋 First 5 rows:")
for r in output[:5]:
    print(f"   {r['Date']} | {r['Description'][:40]} | {r['Amount']}")