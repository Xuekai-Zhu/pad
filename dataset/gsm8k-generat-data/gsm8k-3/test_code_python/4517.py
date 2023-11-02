def solution():
    """A fruit basket consists of 4 bananas, 3 apples, 24 strawberries, 2 avocados, and a bunch of grapes. One banana costs $1. An apple costs $2. 12 strawberries cost $4. An avocado costs $3, and half a bunch of grapes costs $2. What is the total cost of the fruit basket?"""
    # Define the cost of each type of fruit
    BANANA_PRICE = 1
    APPLE_PRICE = 2
    STRAWBERRY_PRICE = 4/12 # cost of 1 strawberry
    AVOCADO_PRICE = 3
    GRAPE_PRICE = 2/0.5 # cost of 1 bunch of grapes

    # Define the number of each type of fruit in the basket
    bananas = 4
    apples = 3
    strawberries = 24
    avocados = 2
    grapes = 1

    # Calculate the total cost of the bananas
    banana_cost = bananas * BANANA_PRICE

    # Calculate the total cost of the apples
    apple_cost = apples * APPLE_PRICE

    # Calculate the total cost of the strawberries
    strawberry_cost = strawberries * STRAWBERRY_PRICE

    # Calculate the total cost of the avocados
    avocado_cost = avocados * AVOCADO_PRICE

    # Calculate the total cost of the grapes
    grape_cost = grapes * GRAPE_PRICE

    # Calculate the total cost of the fruit basket
    total_cost = banana_cost + apple_cost + strawberry_cost + avocado_cost + grape_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())