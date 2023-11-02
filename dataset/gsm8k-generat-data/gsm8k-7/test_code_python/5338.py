def solution():
    shirts_per_hour = 4
    pants_per_hour = 3
    time_shirts = 3
    time_pants = 5

    # Calculate the total number of shirts ironed
    total_shirts = shirts_per_hour * time_shirts

    # Calculate the total number of pants ironed
    total_pants = pants_per_hour * time_pants

    # Calculate the total number of pieces of clothing ironed
    total_clothing = total_shirts + total_pants
    result = total_clothing
    return result

print(solution())