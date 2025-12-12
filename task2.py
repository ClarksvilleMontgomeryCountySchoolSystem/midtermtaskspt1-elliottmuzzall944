# TEST DATA - Do not modify
account_holder = "Taylor Banks"
starting_balance = 487
withdrawal_amount = 120
atm_fee = 3
monthly_fee = 15
months_inactive = 8

# YOUR CODE BELOW THIS LINE
# Calculate remaining balance after fees and withdrawal
# Calculate how many full $20 bills and remaining dollars

# Subtract withdrawal from balance
balance = starting_balance
balance = balance - withdrawal_amount
balance = balance - atm_fee
total_monthly_fees = monthly_fee * months_inactive
balance = balance - total_monthly_fees
full_twenties = balance // 20
remaining_dollars = balance - (full_twenties * 20)

# Subtract ATM fee
# TODO

# Calculate and subtract total monthly fees
# TODO

# Calculate full $20 bills and remaining dollars
#f

# Display results with f-strings
print("Account Holder: Taylor Banks")
print(f"Remaining Balance: ${balance}")
print(f"Full $20 Bills: {full_twenties}")
print(f"Remaining Dollars: ${remaining_dollars}")
