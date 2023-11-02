def solution():
    """Sidney has 4 kittens and 3 adult cats.  She has 7 cans of cat food.  Each adult cat eats 1 can of food per day.  Each kitten eats 3/4 of a can per day.  How many additional cans of food does Sidney need to buy to feed all of her animals for 7 days."""
    # Define the number of cats and kittens
    NUM_KITTENS = 4
    NUM_ADULTS = 3

    # Define the amount of food each cat/kitten needs per day
    KITTEN_FOOD = 0.75
    ADULT_FOOD = 1.0

    # Define the number of days Sidney needs to feed her animals
    NUM_DAYS = 7

    # Define the total amount of food needed per day
    total_food_per_day = (NUM_KITTENS * KITTEN_FOOD) + (NUM_ADULTS * ADULT_FOOD)

    # Calculate the total amount of food needed over the number of days
    total_food_needed = total_food_per_day * NUM_DAYS

    # Calculate the additional cans of food Sidney needs to buy
    additional_food_needed = round(total_food_needed - 7, 2)

    # Display the additional cans of food needed
    result = additional_food_needed
    return result

print(solution())