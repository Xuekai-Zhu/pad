def solution():
    
    # Define the total number of watermelons
    total_watermelons = 120

    # Calculate the number of watermelons ready for harvested after two months
    ready_for_harvest = total_watermelons * 0.3

    # Calculate the number of watermelons remaining after two months
    remaining_watermelons = total_watermelons - ready_for_harvest

    # Calculate the number of watermelons ready for two weeks later
    ready_for_two_weeks = remaining_watermelons * (3/4)

    # Calculate the number of watermelons not ready to be harvested after two weeks
    not_ready_for_two_weeks = remaining_watermelons - ready_for_two_weeks

    # Display the number of watermelons not ready to be harvested
    result = not_ready_for_two_weeks
    return result

print(solution())