def solution():
    # Calculate total milk collected today
    total_today = 365 + 380

    # Calculate total milk collected in two days
    total_milk = total_today + 15

    # Calculate total milk remaining
    remaining_milk = total_milk - 612
    result = remaining_milk
    return result

print(solution())