def solution():
    total_cost = 80  # Viggo spent $80 on a shirt
    num_twenty_bills = x  # Let's call the number of $20 bills x
    num_ten_bills = x - 1  # There is one more $20 bill than $10 bills

    # Use algebra to set up and solve the equation for the total amount paid
    # 20x + 10(x-1) = 80
    # 30x - 10 = 80
    # 30x = 90
    # x = 3
    num_twenty_bills = 3
    num_ten_bills = num_twenty_bills - 1
    result = num_ten_bills
    return result

print(solution())