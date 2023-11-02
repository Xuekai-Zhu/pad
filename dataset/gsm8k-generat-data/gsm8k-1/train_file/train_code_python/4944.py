def solution():
    """300 cows in a field are made up of male and female cows. There are twice as many females as males. Half the females are spotted, and half the males have horns. How many more females with spots are there than males with horns?"""
    total_cows = 300
    male_cows = total_cows / 3
    female_cows = 2 * male_cows
    spotted_females = female_cows / 2
    horned_males = male_cows / 2
    difference = spotted_females - horned_males
    result = difference
    return result

print(solution())