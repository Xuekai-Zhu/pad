def solution():
    
    # Define the amount of weight Joey loses in a single week
    JOEY_LOSS_PER_WEEK = 8

    # Define the number of weeks it takes for Sandy to lose the same amount of weight
    WEEKS = 4

    # Calculate the total weight lost by Joey in 4 weeks
    joey_total_weight_lost = JOEY_LOSS_PER_WEEK * WEEKS

    # Calculate the number of weeks it will take Sandy to lose the same amount of weight
    sandy_weeks_lost = joey_total_weight_lost / (JOEY_LOSS_PER_WEEK / 4)

    # Display the number of weeks it will take Sandy to lose the same amount of weight
    result = sandy_weeks_lost
    return result

print(solution())