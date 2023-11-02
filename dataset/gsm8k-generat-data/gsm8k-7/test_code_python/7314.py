def solution():
    fries_per_potato = 25
    num_potatoes = 15
    total_fries_needed = 200

    # Calculate the total number of fries the chef can make with the given number of potatoes
    total_fries = fries_per_potato * num_potatoes

    # Calculate the number of leftover fries after making 200 fries
    leftover_fries = total_fries - total_fries_needed

    # Calculate the number of leftover potatoes based on the leftover fries
    leftover_potatoes = leftover_fries / fries_per_potato
    result = leftover_potatoes
    return result

print(solution())