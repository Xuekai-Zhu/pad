def solution():
    # Calculate the total number of clothes that need to be washed
    total_clothes = 18 + 12 + 17 + 13

    # Calculate the number of cycles needed to wash all the clothes
    cycles_needed = total_clothes // 15
    if total_clothes % 15 > 0:
        cycles_needed += 1

    # Calculate the total time needed to wash all the clothes in hours
    total_time = cycles_needed * 0.75

    result = total_time
    return result

print(solution())