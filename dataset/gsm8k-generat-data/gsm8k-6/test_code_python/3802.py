def solution():
    # Calculate the total cost of coffee, pastry and cookies for a week
    total_cost = (3.75 + 3.5) * 7 + 5 * 1.25  # cost of latte and croissant for 7 days and 5 cookies

    # Calculate the remaining balance on the gift card
    remaining_balance = 100 - total_cost
    result = remaining_balance
    return result

print(solution())