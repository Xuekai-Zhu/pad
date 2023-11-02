def solution():
    """Michelle loves sugar. She bought 14 chocolate bars, each of which had 10 grams of sugar. She also bought a giant lollipop, which had an additional 37 grams of sugar, plus 190 calories. How many grams of sugar were in all of the candy she bought?"""
    # Define the number of chocolate bars and the sugar content per bar
    chocolate_bars = 14
    sugar_per_bar = 10

    # Calculate the total sugar content of the chocolate bars
    chocolate_sugar = chocolate_bars * sugar_per_bar

    # Define the additional sugar content in the giant lollipop
    lollipop_sugar = 37

    # Calculate the total sugar content of all the candy
    total_sugar = chocolate_sugar + lollipop_sugar

    result = total_sugar
    return result

print(solution())