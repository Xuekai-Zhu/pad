def solution():
    bitcoins = 80  # Jake has 80 bitcoins
    bitcoins -= 20  # Jake donates 20 bitcoins to charity
    bitcoins /= 2  # Jake gives half of his remaining bitcoins to his brother
    bitcoins *= 3  # Jake triples the number of bitcoins he has
    bitcoins -= 10  # Jake donates another 10 coins

    result = bitcoins
    return result

print(solution())