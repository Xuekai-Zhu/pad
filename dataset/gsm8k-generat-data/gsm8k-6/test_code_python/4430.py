def solution():
    # Calculate how much money Barbara has left to save
    money_left = 100 - 20  # Barbara wants a watch that costs $100 and currently has $20

    # Calculate how many more weeks Barbara needs to save
    weeks_needed = money_left // 5  # Barbara gets $5 allowance per week
    result = weeks_needed
    return result

print(solution())