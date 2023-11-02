def solution():
    num_teddies = 5
    num_bunnies = num_teddies * 3
    num_koalas = 1

    # Calculate the number of teddies Jina gets from her mom
    teddy_bonus = num_bunnies * 2

    # Calculate the total number of mascots Jina has
    total_mascots = num_teddies + teddy_bonus + num_bunnies + num_koalas
    result = total_mascots
    return result

print(solution())