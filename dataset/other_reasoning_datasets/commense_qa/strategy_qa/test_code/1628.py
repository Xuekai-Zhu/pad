def solution():
    # Define the maximum amount of food a chipmunk can fit in its mouth and the number of chocolate chips in a tablespoon
    max_food_amount = 2 # tbsp
    chocolate_chips_in_tb = 20 # to 25

    # Calculate the maximum number of chocolate chips a chipmunk can fit in its mouth
    max_chips = max_food_amount * chocolate_chips_in_tb

    # Check if a chipmunk could fit 100 chocolate chips in its mouth
    if max_chips >= 100:
        result = "yes"
    else:
        result = "no"
    
    return result

print(solution())