def solution():
    """Julia has a parrot and a rabbit. She buys food for both of the animals for $30 in total a week. Julia has the rabbit for 5 weeks, and the parrot for 3 weeks. How much money did Julia already spend on food for her animals, if the weekly cost of the rabbit food is $12?"""

    # Define the weekly cost of the rabbit's food
    RABBIT_COST = 12

    # Calculate the total cost of food for both animals
    total_cost = 30 * (5 + 3)

    # Calculate the cost of the rabbit's food
    rabbit_food_cost = RABBIT_COST * 5

    # Calculate the cost of the parrot's food
    parrot_food_cost = total_cost - rabbit_food_cost

    # Display the total cost of both animals' food
    result = total_cost
    return result

print(solution())