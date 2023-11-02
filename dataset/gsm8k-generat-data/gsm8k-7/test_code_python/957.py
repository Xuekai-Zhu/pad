def solution():
    coals_per_grilling = 15
    time_per_grilling = 20  # in minutes
    coals_per_bag = 60
    num_bags = 3

    # Calculate the total number of coals burned by the grill
    total_coals_burned = coals_per_grilling * (time_per_grilling / 20) * coals_per_bag * num_bags

    # Calculate the total time the grill ran in minutes
    total_time = total_coals_burned / coals_per_grilling * time_per_grilling
    result = total_time
    return result

print(solution())