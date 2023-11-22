def solution():
    
    # Define the amount of dog food per feeding and per day
    dog_food_per_feeding = 1
    dog_food_per_day = 2

    # Calculate the total amount of dog food used in the first year
    total_dog_food = dog_food_per_feeding * 180 + dog_food_per_day * 365

    # Calculate the number of bags of dog food used in the first year
    bags_of_food = total_dog_food / 110

    # Display the number of bags of dog food used in the first year
    result = bags_of_food
    return result

print(solution())