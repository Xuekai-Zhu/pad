def solution():
    """Alexa and Emily open up a lemonade stand in the front yard. They spent $10 for lemons, $5 for sugar and $3 for cups.
    The lemonade is $4 a cup. They sell a total of 21 cups. How much profit did Alexa and Emily make after paying off expenses?"""
    # Calculate the total cost of supplies
    total_cost = 10 + 5 + 3

    # Calculate the total revenue from lemonade sales
    total_revenue = 21 * 4

    # Calculate the profit after expenses
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())