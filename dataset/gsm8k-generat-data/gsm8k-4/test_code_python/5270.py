def solution():
    """Cheryl needs 4 cups of basil to make 1 cup of pesto. She can harvest 16 cups of basil from her farm every week for 8 weeks. How many cups of pesto will she be able to make?"""
    
    # Define the amount of basil needed to make 1 cup of pesto
    basil_per_pesto = 4
    
    # Define the total amount of basil harvested in 8 weeks
    total_basil_harvested = 16 * 8
    
    # Calculate the total amount of pesto that can be made
    cups_of_pesto = total_basil_harvested // basil_per_pesto
    
    result = cups_of_pesto
    return result

print(solution())