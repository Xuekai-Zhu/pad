def solution():
    num_plants = 18
    num_tomatoes_per_plant = 7

    # Calculate the total number of tomatoes from all plants
    total_tomatoes = num_plants * num_tomatoes_per_plant

    # Calculate the number of tomatoes that Andy dries
    num_dried_tomatoes = total_tomatoes / 2

    # Calculate the number of tomatoes remaining after drying
    num_remaining_tomatoes = total_tomatoes - num_dried_tomatoes

    # Calculate the number of tomatoes that Andy turns into marinara sauce
    num_marinara_tomatoes = num_remaining_tomatoes / 3

    # Calculate the number of tomatoes left after making marinara sauce
    num_tomatoes_left = num_remaining_tomatoes - num_marinara_tomatoes
    result = num_tomatoes_left
    return result

print(solution())