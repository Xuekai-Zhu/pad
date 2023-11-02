def solution():
    # Calculate the total eggs collected in a week
    eggs_collected = 2 * 8 * 12

    # Calculate the total eggs used for delivery and making pies
    eggs_used = 3 * 12 + 5 * 12 + 4 * 12

    # Calculate the eggs remaining
    eggs_remaining = eggs_collected - eggs_used

    # Calculate the eggs donated to charity
    eggs_donated = eggs_remaining % 12

    result = eggs_donated
    return result

print(solution())