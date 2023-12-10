#!/usr/bin/python3

import sys

for line in sys.stdin:
    # Assuming each line contains transaction information
    fields = line.strip().split(',')
    
    # Make sure the line has the expected number of fields
    if len(fields) == 8:
        customer_id = fields[6]
        
        # Ensure the fields 3 and 4 are present and non-empty
        if fields[3] and fields[4]:
            try:
                # Try to convert fields 3 and 4 to float and int, respectively
                transaction_amount = int(fields[3]) * float(fields[5])
                print(f"{customer_id}\t{transaction_amount}")
            except ValueError as e:
                # Handle the case where conversion fails
                sys.stderr.write(f"Error processing line: {line}\n")
                sys.stderr.write(f"Error details: {e}\n")
        else:
            # Handle the case where fields 3 or 4 are empty
            sys.stderr.write(f"Error processing line: {line}\n")
            sys.stderr.write("Quantity or UnitPrice is missing or empty\n")
    else:
        # Handle the case where the line doesn't have the expected number of fields
        sys.stderr.write(f"Error processing line: {line}\n")
        sys.stderr.write("Incorrect number of fields\n")
