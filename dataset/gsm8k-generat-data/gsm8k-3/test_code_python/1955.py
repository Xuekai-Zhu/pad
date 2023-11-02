def solution():
    """Ned opens a left-handed store.  He sells left-handed mice.  They cost 30% more than normal mice.  He sells 25 a day and his store is open every day except Sunday, Thursday, and Friday.  If normal mice cost $120 how much money does he make a week?"""
    # Define the cost of a normal mouse and the markup for a left-handed mouse
    NORMAL_MOUSE_COST = 120
    LEFT_HANDED_MOUSE_MARKUP = 0.3

    # Calculate the cost of a left-handed mouse
    left_handed_mouse_cost = NORMAL_MOUSE_COST + (NORMAL_MOUSE_COST * LEFT_HANDED_MOUSE_MARKUP)

    # Calculate the total sales for a day
    daily_sales = left_handed_mouse_cost * 25

    # Calculate the total sales for a week
    days_open = 7 - 3 - 1 - 1  # Subtract the days the store is closed
    weekly_sales = daily_sales * days_open

    # Display the total sales for the week
    result = weekly_sales
    return result

print(solution())