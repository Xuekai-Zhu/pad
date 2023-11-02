def solution():
    num_tomato_plants = 6
    num_eggplant_plants = 2
    num_pepper_plants = 4

    # Calculate the number of remaining tomato plants after half died
    num_remaining_tomatoes = num_tomato_plants // 2

    # Calculate the total number of vegetables from the remaining tomato plants
    tomato_veggies = num_remaining_tomatoes * 7

    # Calculate the total number of vegetables from the eggplant plants
    eggplant_veggies = num_eggplant_plants * 7

    # Calculate the number of remaining pepper plants after one died
    num_remaining_peppers = num_pepper_plants - 1

    # Calculate the total number of vegetables from the remaining pepper plants
    pepper_veggies = num_remaining_peppers * 7

    # Calculate the total number of vegetables in the garden
    total_veggies = tomato_veggies + eggplant_veggies + pepper_veggies
    result = total_veggies
    return result

print(solution())