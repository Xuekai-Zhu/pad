def solution():
    """Regina has a farm with animals. She has 20 cows and four times more pigs. Someone told her, that she could sell all the animals and earn $400 for each pig and $800 for each cow. How much money would she earn if she would sell all the animals from the farm?"""
    cows = 20
    pigs = 4 * cows
    cow_earnings = cows * 800
    pig_earnings = pigs * 400
    total_earnings = cow_earnings + pig_earnings
    result = total_earnings
    return result

print(solution())