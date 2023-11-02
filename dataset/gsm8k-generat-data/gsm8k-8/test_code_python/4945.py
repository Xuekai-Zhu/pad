def solution():
    # Define the number of cows and the ratio of females to males
    total_cows = 300
    female_to_male_ratio = 2

    # Calculate the number of females and males
    total_females = (female_to_male_ratio / (1 + female_to_male_ratio)) * total_cows
    total_males = total_cows - total_females

    # Calculate the number of females with spots and males with horns
    females_with_spots = (1/2) * total_females
    males_with_horns = (1/2) * total_males

    # Calculate the difference between the two groups
    difference = females_with_spots - males_with_horns
    result = difference
    return result

print(solution())