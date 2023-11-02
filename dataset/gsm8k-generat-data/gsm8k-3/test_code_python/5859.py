def solution():
    """Michelle bought 14 chocolate bars, each of which had 10 grams of sugar. She also bought a giant lollipop, which had an additional 37 grams of sugar, plus 190 calories. How many grams of sugar were in all of the candy she bought?"""
    # Define the number of chocolate bars and the amount of sugar in each
    num_bars = 14
    sugar_per_bar = 10

    # Calculate the total amount of sugar in the chocolate bars
    chocolate_sugar = num_bars * sugar_per_bar

    # Define the amount of sugar in the giant lollipop
    lollipop_sugar = 37

    # Calculate the total amount of sugar in all the candy Michelle bought
    total_sugar = chocolate_sugar + lollipop_sugar

    # Display the total amount of sugar
    result = total_sugar
    return result

print(solution())