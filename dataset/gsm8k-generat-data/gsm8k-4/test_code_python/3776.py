def solution():
    """Julia has a parrot and a rabbit. She buys food for both of the animals for $30 in total a week. Julia has the rabbit for 5 weeks, and the parrot for 3 weeks. How much money did Julia already spend on food for her animals, if the weekly cost of the rabbit food is $12?"""
    # Define the weekly cost of food for the rabbit
    rabbit_food_cost = 12

    # Calculate the weekly cost of food for the parrot
    parrot_food_cost = 30 - rabbit_food_cost

    # Calculate the total cost of food for the rabbit for 5 weeks
    rabbit_food_total = rabbit_food_cost * 5

    # Calculate the total cost of food for the parrot for 3 weeks
    parrot_food_total = parrot_food_cost * 3

    # Calculate the total cost of food for both animals
    total_cost = rabbit_food_total + parrot_food_total

    # Return the result
    result = total_cost
    return result

print(solution())