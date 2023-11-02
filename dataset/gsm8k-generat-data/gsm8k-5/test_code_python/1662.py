def solution():
    total_tomatoes = 100  # There are 100 tomatoes on the plant
    picked_tomatoes = total_tomatoes / 4  # Jane picks 1/4 of the tomatoes

    # Calculate the number of tomatoes remaining after the first picking
    remaining_tomatoes = total_tomatoes - picked_tomatoes

    # Jane picks 20 more tomatoes the following week
    remaining_tomatoes -= 20

    # Jane picks twice the number of tomatoes the third week
    remaining_tomatoes -= 2 * picked_tomatoes

    result = remaining_tomatoes
    return result

print(solution())