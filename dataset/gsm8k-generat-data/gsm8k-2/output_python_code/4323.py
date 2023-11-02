def solution():
    """Carmela has $7 and each of her four cousins has $2. How much will Carmela have to give to each of her cousins so that she and her cousins will have the same amount of money?"""
    carmela_money = 7
    cousins_money = 2
    total_people = 5
    difference = cousins_money - (carmela_money/total_people)
    result = round(difference, 2)
    return result

print(solution())