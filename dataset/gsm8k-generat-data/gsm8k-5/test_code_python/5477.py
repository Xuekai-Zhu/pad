def solution():
    cows = 20
    pigs = 4 * cows

    # Calculate the total amount of money Regina would earn if she sold all the animals
    total_money = (pigs * 400) + (cows * 800)

    result = total_money
    return result

print(solution())