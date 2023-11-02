def solution():
    # Calculate Rica's prize money
    rica_percentage = 3/8
    rica_money = rica_percentage * total_money  # let's assume total prize money to be unknown variable total_money

    # Calculate the amount of money Rica spent
    rica_spent = (1/5) * rica_money

    # Calculate the remaining money Rica has
    rica_remaining = rica_money - rica_spent

    # Use the remaining money to find the total prize money won by Rica's group
    total_remaining_percentage = 1 - rica_percentage
    total_remaining = rica_remaining / total_remaining_percentage
    result = total_remaining
    return result

print(solution())