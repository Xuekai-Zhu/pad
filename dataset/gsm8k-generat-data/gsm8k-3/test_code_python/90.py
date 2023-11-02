def solution():
    """Herman likes to feed the birds in December, January and February. He feeds them 1/2 cup in the morning and 1/2 cup in the afternoon. How many cups of food will he need for all three months?"""
    # Define the number of months
    num_months = 3

    # Define the amount of food per feeding
    food_per_feeding = 0.5

    # Calculate the total amount of food needed for one day
    total_food_per_day = food_per_feeding * 2

    # Calculate the total amount of food needed for one month
    total_food_per_month = total_food_per_day * 30

    # Calculate the total amount of food needed for all three months
    total_food = total_food_per_month * num_months

    # return the result
    result = total_food
    return result

print(solution())