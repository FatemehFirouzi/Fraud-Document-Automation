import os
import pandas as pd

# Load data
df = pd.read_csv("data/sample_cases.csv")

# Create output folder
output_folder = "data/output_docs"
os.makedirs(output_folder, exist_ok=True)

# Generate reports
for _, row in df.iterrows():
    file_name = f"{output_folder}/case_{row['case_id']}.txt"

    with open(file_name, "w") as f:
        f.write("Fraud Operations Case Review\n")
        f.write("=" * 35 + "\n\n")
        f.write(f"Case ID: {row['case_id']}\n")
        f.write(f"Customer ID: {row['customer_id']}\n")
        f.write(f"Total Transactions: {row['total_transactions']}\n")
        f.write(f"Total Returns: {row['total_returns']}\n")
        f.write(f"Total Disputes: {row['total_disputes']}\n")
        f.write(f"Risk Level: {row['risk_flag']}\n\n")
        f.write("Review Notes:\n")
        f.write(row['review_note'])

print("Documents generated successfully.")