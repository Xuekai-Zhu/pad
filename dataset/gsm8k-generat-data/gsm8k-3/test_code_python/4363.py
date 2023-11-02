def solution():
    """Fabian is shopping at a nearby supermarket. He wants to buy 5 kilograms of apples, 3 packs of sugar, and 500 grams of walnuts. One kilogram of apples costs $2, and one kilogram of walnuts costs $6. One pack of sugar is $1 cheaper than one kilogram of apples. How much Fabian needs to pay for the items he wants to buy?"""
    # Define the cost of each item
    APPLE_PRICE = 2
    SUGAR_PRICE = APPLE_PRICE - 1
    WALNUT_PRICE = 6

    # Define the amount of each item Fabian wants to buy
    apple_kgs = 5
    sugar_packs = 3
    walnut_grams = 500

    # Calculate the total cost of the apples
    apple_cost = APPLE_PRICE * apple_kgs

    # Calculate the total cost of the sugar
    sugar_cost = SUGAR_PRICE * apple_kgs * sugar_packs

    # Convert the amount of walnuts from grams to kilograms and calculate the total cost
    walnut_cost = WALNUT_PRICE * (walnut_grams / 1000)

    # Calculate the total cost of all the items
    total_cost = apple_cost + sugar_cost + walnut_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())