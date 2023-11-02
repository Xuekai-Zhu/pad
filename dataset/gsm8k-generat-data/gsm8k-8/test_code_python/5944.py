def solution():
    # Define the number of rows and the expected yield for each crop
    corn_rows = 10
    pot_rows = 5
    corn_yield = 9
    pot_yield = 30
    
    # Calculate the total expected yield before the pest damage
    total_yield = (corn_rows * corn_yield) + (pot_rows * pot_yield)
    
    # Calculate the number of crops remaining after the pests have destroyed half
    remaining_yield = total_yield * 0.5
    
    result = remaining_yield
    return result

print(solution())