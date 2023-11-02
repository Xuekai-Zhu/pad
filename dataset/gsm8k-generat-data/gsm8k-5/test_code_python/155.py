def solution():
    total_mangoes = 60
    sold_market = 20
    sold_community = (total_mangoes - sold_market) / 2
    
    # Calculate the total number of mangoes
    total_sold = sold_market + sold_community
    
    # Calculate the number of mangoes per kilogram
    mangoes_per_kg = 8
    
    # Calculate the total number of mangoes he still has
    mangoes_left = (total_mangoes - total_sold) * mangoes_per_kg
    
    result = mangoes_left
    return result

print(solution())