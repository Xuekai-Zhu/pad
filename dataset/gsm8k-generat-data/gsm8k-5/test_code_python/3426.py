def solution():
    # Lorie has 2 pieces of $100 bills
    # First, one piece is changed to $50 bills, leaving her with one piece of $100 bills and one piece of $50 bills
    # Half of the remaining $100 bill (which is $50) is changed to $10 bills, leaving her with $25 in $100 bills, $50 in $50 bills, $25 in $10 bills
    # The remaining $25 in $100 bills is changed to $5 bills, leaving her with $50 in $5 bills
    total_bills = 2  # Lorie has 2 pieces of $100 bills
    total_bills += 1  # After changing one piece of $100 bills to $50 bills, she has two pieces of bills
    total_bills += 2  # After changing half of the remaining $100 bill to $10 bills, she has two more pieces of bills
    total_bills += 5  # After changing the remaining $25 in $100 bills to $5 bills, she has five more pieces of bills
    result = total_bills
    return result

print(solution())