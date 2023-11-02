def solution():
    """Danny has 3 bottles of soda. He drinks 90% of one bottle and gives 70% of the other two bottles to his friends. How much soda does Danny have left, expressed as a percentage of a bottle?"""
    total_soda = 3
    soda_drunk = 0.9
    soda_given = 0.7 * 2
    soda_left = (total_soda - 1 + soda_given) * (1 - soda_drunk)
    percentage_left = soda_left / 1 * 100
    result = percentage_left
    return result

print(solution())