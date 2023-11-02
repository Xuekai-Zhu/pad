def solution():
    starting_mice = 8  # Billy starts with 8 mice
    pups_per_mice = 6  # Each mouse has 6 pups
    adult_mice = starting_mice + (starting_mice * pups_per_mice)  # Mice that grew up and had their own pups
    total_pups = adult_mice * pups_per_mice  # Total number of pups
    adult_mice_after_stress = adult_mice - (adult_mice * 2)  # Subtract the mice that ate their own pups due to stress
    total_mice = adult_mice_after_stress + total_pups  # Add the remaining adult mice and pups to get the total number of mice

    result = total_mice
    return result

print(solution())