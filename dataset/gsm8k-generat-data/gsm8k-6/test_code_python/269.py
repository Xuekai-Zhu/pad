def solution():
    # Calculate the total amount of money John has earned
    total_earned = 18 + (1/2)*18 + 20  # earned $18 on Saturday, half of that on Sunday, and $20 the previous weekend

    # Calculate the amount of money John still needs to earn
    remaining_money = 60 - total_earned

    result = remaining_money
    return result

print(solution())