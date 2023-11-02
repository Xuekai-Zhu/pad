def solution():
    # Define the variables
    total_geese = 12
    landed_geese = total_geese // 2
    new_geese = 4

    # Calculate the number of geese in the first V formation
    first_v_geese = total_geese + landed_geese + new_geese
    result = first_v_geese
    return result

print(solution())