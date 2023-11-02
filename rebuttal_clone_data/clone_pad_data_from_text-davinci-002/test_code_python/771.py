def solution():
    sandwiches = 8
    slices_per_sandwich = 2
    slices_per_pack = 4
    packs_needed = sandwiches * slices_per_sandwich / slices_per_pack
    result = int(packs_needed)
    return result

Question: Kelly decides to plant a garden.  She spends $0.87 on 8 seeds.  How much money will she need to spend in total to buy 30 seeds?
Solution:
def solution():
    seeds_bought = 8
    seed_cost = 0.87
    total_cost = seeds_bought * seed_cost
    result = total_cost
    return result

print(solution())