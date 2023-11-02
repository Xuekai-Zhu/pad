def solution():
    num_flowering_plants = 7
    num_fruiting_plants = 2*num_flowering_plants

    # Roxy buys 3 flowering plants and 2 fruiting plants
    num_flowering_plants += 3
    num_fruiting_plants += 2

    # Roxy gives away 1 flowering plant and 4 fruiting plants
    num_flowering_plants -= 1
    num_fruiting_plants -= 4

    # Calculate the total number of plants remaining
    total_plants = num_flowering_plants + num_fruiting_plants
    result = total_plants
    return result

print(solution())