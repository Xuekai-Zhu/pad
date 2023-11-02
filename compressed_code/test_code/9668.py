def solution():
    
    total_cows = 300
    male_cows = total_cows / 3
    female_cows = 2 * male_cows
    spotted_females = female_cows / 2
    horned_males = male_cows / 2
    difference = spotted_females - horned_males
    result = difference
    return result

print(solution())