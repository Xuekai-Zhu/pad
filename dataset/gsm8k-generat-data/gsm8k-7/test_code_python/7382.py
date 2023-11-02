def solution():
    num_people = 5
    serving_size = 16  # 1 pound is 16 ounces
    steak_size = 20

    # Calculate the total amount of steak needed in ounces
    total_steak_needed = num_people * serving_size

    # Calculate the number of steaks needed
    num_steaks_needed = total_steak_needed / steak_size

    # Round up to the nearest whole number
    num_steaks_needed = math.ceil(num_steaks_needed)
    result = num_steaks_needed
    return result

print(solution())