def solution():
    num_hearts_per_card = 4
    num_cards = 52
    num_cows = num_hearts_per_card * num_cards * 2
    cow_cost = 200
    total_cost = num_cows * cow_cost
    result = total_cost
    return result

print(solution())