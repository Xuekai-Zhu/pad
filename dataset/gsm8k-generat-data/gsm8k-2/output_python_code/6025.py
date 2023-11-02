def solution():
    """John buys 3 boxes of burritos. He gives away a 3rd of them to his friend. Each box has 20 burritos. He eats 3 burritos per day for 10 days. How many burritos does he have left?"""
    total_burritos = 3 * 20
    given_away = total_burritos / 3
    remaining_burritos = total_burritos - given_away
    eaten_burritos = 3 * 10
    final_burritos = remaining_burritos - eaten_burritos
    result = final_burritos
    return result

print(solution())