def solution():
    
    # Define the percentage of boys in a school population
    BOYS_PERCENTAGE = 40

    # Calculate the total population
    total_population = 240 / (100 - BOYS_PERCENTAGE) / 100

    # Calculate the number of girls in the school
    girls = total_population - 240

    # Display the number of girls
    result = girls
    return result

print(solution())