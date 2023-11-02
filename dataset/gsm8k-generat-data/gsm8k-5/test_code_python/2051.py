def solution():
    apples_per_pie = 8  # Each pie needs 8 apples
    pies_to_bake = 10  # Mary wants to bake 10 apple pies
    apples_harvested = 50  # Mary already harvested 50 apples

    # Calculate the total number of apples needed for all the pies
    total_apples_needed = pies_to_bake * apples_per_pie

    # Calculate the number of additional apples Mary needs to buy
    additional_apples_needed = total_apples_needed - apples_harvested
    result = additional_apples_needed
    return result

print(solution())