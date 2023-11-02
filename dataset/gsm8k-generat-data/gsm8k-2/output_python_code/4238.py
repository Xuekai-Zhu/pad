def solution():
    """Alex was having a cookout Friday night and planned to serve burgers to his guests. He planned to cook 3 burgers for each guest and had invited 10 friends over. 1 of his friends didn't eat meat and said they would bring their own food. Another one of his friends didn't eat bread and would not need the buns. The burger buns came 8 to a pack. How many packs of buns did Alex need to buy?"""
    total_gest_burgers = 30 # 10 x 3 burgers
    total_buns = total_gest_burgers * 2 # 2 buns per burgers
    total_buns -= 8 # minus 1 friend who brought their own food
    total_buns -= 8 # minus 1 friend who didn't eat buns
    necessary_bun_packs = (total_buns // 8) + int(total_buns % 8 > 0) # Each pack has 8 buns
    result = necessary_bun_packs
    return result

print(solution())