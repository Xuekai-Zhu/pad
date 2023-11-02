def solution():
    # Calculate the total number of clothes
    total_clothes = 18 + 12 + 17 + 13  

    # Calculate the number of cycles needed
    num_cycles = total_clothes // 15
    if total_clothes % 15 != 0:
        num_cycles += 1

    # Calculate the total time needed in hours
    total_time = num_cycles * 0.75  # Each cycle takes 45 minutes

    result = total_time
    return result

print(solution())