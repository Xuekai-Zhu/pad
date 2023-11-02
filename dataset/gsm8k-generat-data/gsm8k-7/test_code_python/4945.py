def solution():
    total_cows = 300
    female_to_male_ratio = 2
    male_with_horns_ratio = 0.5

    # Calculate the number of females and males
    num_females = (total_cows / (female_to_male_ratio + 1)) * female_to_male_ratio
    num_males = total_cows - num_females

    # Calculate the number of females with spots and males with horns
    num_females_with_spots = num_females * 0.5
    num_males_with_horns = num_males * male_with_horns_ratio

    # Calculate the difference between the number of females with spots and males with horns
    difference = num_females_with_spots - num_males_with_horns
    result = difference
    return result

print(solution())