def solution():
    """Oliver has $40 and 200 quarters. If he gives his sister $5 and 120 quarters, how much money in total is he left with?"""
    # Calculate the total amount of money Oliver has in dollars
    total_money = 40 + (200 * 0.25) 

    # Calculate the amount of money Oliver's sister takes
    money_taken = 5 + (120 * 0.25)

    # Calculate the amount of money Oliver is left with
    remaining_money = total_money - money_taken

    # Convert the remaining money back to dollars and cents
    dollars = remaining_money // 1
    cents = (remaining_money % 1) * 100

    # Display the remaining amount of money in dollars and cents
    result = f"${dollars:.0f}.{cents:.0f}"
    return result

print(solution())