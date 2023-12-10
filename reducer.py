#!/usr/bin/python3

import sys
import csv

current_customer = None
total_transaction_amount = 0
all_customers = []


for line in sys.stdin:
    try:
        # Split the input line into customer_id and transaction_amount
        customer_id, transaction_amount = line.strip().split('\t')
        if(customer_id==None and len(customer_id) == 0):
            continue
        transaction_amount = float(transaction_amount)

        # Check if the customer_id is the same as the current_customer
        if current_customer == customer_id:
            total_transaction_amount += transaction_amount
        else:
            # If a new customer is encountered, add the previous customer's data to the list
            if current_customer:
                all_customers.append((current_customer, total_transaction_amount))

            # Update current_customer and reset total_transaction_amount
            current_customer = customer_id
            total_transaction_amount = transaction_amount

    except ValueError as e:
        # Handle the case where conversion to float fails
        sys.stderr.write(f"Error processing line: {line}")
        sys.stderr.write(f"Error details: {e}\n")

# Print the final result for the last customer
if current_customer:
    all_customers.append((current_customer, total_transaction_amount))

# Sort the customers based on total transaction amount in descending order
sorted_customers = sorted(all_customers, key=lambda x: x[1], reverse=True)

# Calculate the threshold for the top 10%
total_customers = len(sorted_customers)
top_10_percent_threshold = int(0.1 * total_customers)

#outputting the data to the system output
print("CUSTOMER_ID,TOTAL_TRANSACTION_AMT")
for customer_id, total_amount in sorted_customers[:top_10_percent_threshold]:
    # Print CSV-formatted line to standard output
    print(f"{str(customer_id)},{str(total_amount)}")

