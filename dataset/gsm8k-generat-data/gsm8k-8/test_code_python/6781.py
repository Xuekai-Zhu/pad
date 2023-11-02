def solution():
    # Calculate the number of plants in the original plan
    original_plan = 7 * 18

    # Calculate the total number of plants with the addition
    total_plants = original_plan + 15

    # Calculate the number of plants Papi Calot needs to buy
    plants_to_buy = total_plants - original_plan
    result = plants_to_buy
    return result

print(solution())