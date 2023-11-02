def solution():
    """Kaylee needs to sell 33 boxes of biscuits. So far, she has sold 12 boxes of lemon biscuits to her aunt, 5 boxes of chocolate biscuits to her mother, and 4 boxes of oatmeal biscuits to a neighbor. How many more boxes of biscuits does Kaylee need to sell?"""
    # Define the number of boxes of each type of biscuit sold
    lemon_sold = 12
    chocolate_sold = 5
    oatmeal_sold = 4

    # Calculate the total number of boxes sold
    total_sold = lemon_sold + chocolate_sold + oatmeal_sold

    # Calculate the number of boxes still needed to be sold
    remaining = 33 - total_sold

    # Display the number of boxes still needed to be sold
    result = remaining
    return result

print(solution())