def solution():
    """Jake amasses a fortune of 80 bitcoin. He donates 20 bitcoins to charity. He then gives half of all the bitcoins to his brother. After that, he triples the number of bitcoins he has. Then he donates another 10 coins. How many coins does he have?"""
    initial_coins = 80
    donated_coins = 20
    remaining_coins = initial_coins - donated_coins
    half_coins = remaining_coins / 2
    tripled_coins = half_coins * 3
    final_coins = tripled_coins - 10
    result = final_coins
    return result

print(solution())