def solution():
    # Define the weight of each dog
    dog1_weight = 20
    dog2_weight = 40
    dog3_weight = 10
    dog4_weight = 30
    dog5_weight = 50

    # Calculate the total amount of dog food needed per day
    total_weight = dog1_weight + dog2_weight + dog3_weight + dog4_weight + dog5_weight
    total_food_needed = total_weight // 10

    result = total_food_needed
    return result

print(solution())