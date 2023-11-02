def solution():
    """40% of a farmer's cattle are males. The rest are females. If a female cow produces 2 gallons of milk a day, how much milk will the farmer get a day if he has 50 male cows?"""
    total_cows = 100
    males = 40
    females = 60
    male_cows = 50
    female_cows = total_cows * (females / 100)
    milk_from_females = female_cows * 2
    total_milk = milk_from_females
    result = total_milk
    return result

print(solution())