def solution():
    
    # Define the number of legs for each type of insect
    SPIDER_LEGS = 8
    INSECT_LEGS = 6
    MORE_INVERTEBRATE_LEGS = 10

    # Define the number of each type of insect
    spiders = 80
    insects = 90
    rare_invertebrates = 3

    # Calculate the total number of legs
    total_legs = (spiders * SPIDER_LEGS) + (insects * INSECT_LEGS) + (rare_invertebrates * MORE_INVERTEBRATE_LEGS)

    # Display the total number of legs
    result = total_legs
    return result

print(solution())