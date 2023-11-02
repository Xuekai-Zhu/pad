def solution():
    """Leila eats cake almost every week. Last week, she ate 6 cakes on Monday, 9 cakes on Friday, and on Saturday, she ate triple the number of cakes she ate on Monday. How many cakes does Leila eat?"""
    # Define the number of cakes eaten on Monday and Friday
    cakes_monday = 6
    cakes_friday = 9

    # Calculate the number of cakes eaten on Saturday
    cakes_saturday = cakes_monday * 3

    # Calculate the total number of cakes eaten
    total_cakes = cakes_monday + cakes_friday + cakes_saturday

    # Display the total number of cakes eaten
    result = total_cakes
    return result

print(solution())