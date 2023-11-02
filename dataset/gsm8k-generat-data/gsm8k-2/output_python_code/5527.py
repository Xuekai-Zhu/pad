def solution():
    """40% of a farmer's cattle are males. The rest are females. If a female cow produces 2 gallons of milk a day, how much milk will the farmer get a day if he has 50 male cows?"""
    total_cattle = 100
    male_cattle = 40
    female_cattle = 60
    male_cows = 50
    female_cows = female_cattle - male_cows
    milk_per_female_cow = 2
    total_milk = female_cows * milk_per_female_cow
    result = total_milk
    return result

print(solution())