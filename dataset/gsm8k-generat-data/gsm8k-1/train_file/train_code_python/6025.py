def solution():
    """John buys 3 boxes of burritos. He gives away a 3rd of them to his friend. Each box has 20 burritos. He eats 3 burritos per day for 10 days. How many burritos does he have left?"""
    boxes = 3
    burritos_per_box = 20
    total_burritos = boxes * burritos_per_box
    given_away = total_burritos // 3
    remaining_burritos = total_burritos - given_away
    days = 10
    burritos_eaten = 3 * days
    burritos_left = remaining_burritos - burritos_eaten
    result = burritos_left
    return result

print(solution())