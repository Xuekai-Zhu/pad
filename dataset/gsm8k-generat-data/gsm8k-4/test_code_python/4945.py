def solution():
    """300 cows in a field are made up of male and female cows. There are twice as many females as males. Half the females are spotted, and half the males have horns. How many more females with spots are there than males with horns?"""
    # Define the total number of cows and the ratio of females to males
    total_cows = 300
    female_male_ratio = 2

    # Calculate the number of females and males
    females = (total_cows / (1 + female_male_ratio))
    males = total_cows - females

    # Calculate the number of females with spots and males with horns
    females_spotted = females / 2
    males_horned = males / 2

    # Calculate the difference between the number of females with spots and males with horns
    difference = females_spotted - males_horned

    # Return the result
    result = int(difference)
    return result

print(solution())