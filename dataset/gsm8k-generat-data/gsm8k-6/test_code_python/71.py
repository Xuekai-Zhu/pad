def solution():
    # Calculate the total revenue from selling crafts
    total_revenue = 3 * 12  # Hillary sold 3 crafts for 12 dollars each

    # Add the extra 7 dollars from the appreciative customer
    total_revenue += 7

    # Subtract the 18 dollars Hillary deposited into her bank account
    left_with = total_revenue - 18
    result = left_with
    return result

print(solution())