def solution():
    """Mr. Doré bought $140 worth of pants, a $43 shirt and a $15 tie. He pays with a $200 bill. How much will the saleswoman give him back?"""
    # Calculate the total cost of the items purchased
    total_cost = 140 + 43 + 15

    # Calculate the amount of change due
    change_due = 200 - total_cost

    # Display the amount of change due
    result = change_due
    return result

print(solution())