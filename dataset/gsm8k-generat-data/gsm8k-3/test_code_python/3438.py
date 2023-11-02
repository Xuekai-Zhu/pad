def solution():
    """Penn operates an ice cream stall for a week. On the first day, she made $10. Every day after that, she made $4 more than the previous day. How much money did Penn make after 5 days?"""

    # Initialize variables
    day = 1
    money = 10

    # Iterate over 5 days
    while day <= 5:
        money += 4*(day-1)
        day += 1

    # Display the total money made
    result = money
    return result

print(solution())