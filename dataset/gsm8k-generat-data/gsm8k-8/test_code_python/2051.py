def solution():
    # Define the number of pies and apples needed per pie
    num_pies = 10
    apples_per_pie = 8

    # Calculate the total number of apples needed for all the pies
    total_apples_needed = num_pies * apples_per_pie

    # Subtract the number of apples already harvested to find the number of apples Mary needs to buy
    apples_to_buy = total_apples_needed - 50
    result = apples_to_buy
    return result

print(solution())