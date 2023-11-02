def solution():
    """Half of Jerome's money was $43. He gave $8 to Meg and thrice as much to Bianca. How much does Jerome have left?"""
    # Calculate Jerome's total money
    total_money = 43 * 2

    # Calculate the amount of money given to Meg
    meg_money = 8

    # Calculate the amount of money given to Bianca
    bianca_money = meg_money * 3

    # Calculate Jerome's remaining money
    remaining_money = total_money - (meg_money + bianca_money)

    # Display Jerome's remaining money
    result = remaining_money
    return result

print(solution())