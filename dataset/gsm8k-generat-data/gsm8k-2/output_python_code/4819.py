def solution():
    """Danny has 3 bottles of soda. He drinks 90% of one bottle and gives 70% of the other two bottles to his friends. How much soda does Danny have left, expressed as a percentage of a bottle?"""
    total_soda = 3
    drank_soda = 0.9
    given_soda = 0.7 * 2
    remaining_soda = total_soda - drank_soda - given_soda
    remaining_percentage = (remaining_soda / total_soda) * 100
    result = remaining_percentage
    return result

print(solution())