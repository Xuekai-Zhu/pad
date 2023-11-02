def solution():
    num_friends = 3
    num_green_sweets = 212
    num_blue_sweets = 310
    num_yellow_sweets = 502

    # Calculate the total number of sweets
    total_sweets = num_green_sweets + num_blue_sweets + num_yellow_sweets

    # Calculate the number of sweets each person will get
    num_sweets_per_person = total_sweets / (num_friends + 1)

    result = num_sweets_per_person
    return result

print(solution())