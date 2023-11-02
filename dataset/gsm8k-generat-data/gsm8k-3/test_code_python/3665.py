def solution():
    """A snack machine accepts only quarters. Candy bars cost ¢25, each piece of chocolate costs ¢75, and a pack of juice costs ¢50. How many quarters are needed to buy three candy bars, two pieces of chocolate, and one pack of juice?"""
    # Define the prices in cents
    CANDY_PRICE = 25
    CHOCOLATE_PRICE = 75
    JUICE_PRICE = 50

    # Define the number of items purchased
    candy_bars = 3
    chocolates = 2
    juice_packs = 1

    # Calculate the total cost in cents
    total_cost = (candy_bars * CANDY_PRICE) + (chocolates * CHOCOLATE_PRICE) + (juice_packs * JUICE_PRICE)

    # Calculate the number of quarters needed
    quarters = total_cost // 25

    # Display the number of quarters needed
    result = quarters
    return result

print(solution())