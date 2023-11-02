def solution():
    # Define the number of cartons already in Emilia's cupboard
    strawberries_in_cupboard = 2
    blueberries_in_cupboard = 7

    # Define the total number of cartons of berries needed
    total_cartons_needed = 42

    # Calculate the number of cartons Emilia should buy
    cartons_to_buy = total_cartons_needed - strawberries_in_cupboard - blueberries_in_cupboard
    result = cartons_to_buy
    return result

print(solution())