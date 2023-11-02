def solution():
    """Ned opens a left-handed store. He sells left-handed mice. They cost 30% more than normal mice. He sells 25 a day and his store is open every day except Sunday, Thursday, and Friday.
    If normal mice cost $120, how much money does he make a week?"""
    # Define the variables and constants
    normal_price = 120
    left_handed_price = normal_price * 1.3
    left_handed_mice_sold = 25
    days_open = 7 - 3  # days open in a week (excluding Sunday, Thursday, and Friday)

    # Calculate the total revenue from selling left-handed mice in a week
    total_revenue = left_handed_price * left_handed_mice_sold * days_open

    # Calculate the profit (total revenue minus the cost of normal mice) in a week
    profit = total_revenue - (normal_price * left_handed_mice_sold * days_open)

    # return the result
    result = round(profit)
    return result

print(solution())