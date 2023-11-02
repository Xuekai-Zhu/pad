def solution():
    
    # Define the weight Martin eats each day for breakfast
    Cheerios_weight = 1.25
    donuts_weight = 1.75

    # Define the number of days in 5 weeks
    days = 5

    # Calculate Martin's weight after 5 weeks
    weight_after_5_weeks = Cheerios_weight - (cheerios_weight * days) + donuts_weight

    # Calculate the difference in his weight between the two breakfast options
    weight_difference = weight_after_5_weeks - weight_after_5_weeks

    # Display the weight difference
    result = weight_difference
    return result

print(solution())