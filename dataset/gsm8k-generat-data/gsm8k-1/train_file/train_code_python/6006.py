def solution():
    """A garden store sells packages of pumpkin seeds for $2.50, tomato seeds for $1.50, and chili pepper seeds for $0.90. Harry is planning to plant three different types of vegetables on his farm. How much will Harry have to spend if he wants to buy three packets of pumpkin seeds, four packets of tomato seeds, and five packets of chili pepper seeds?"""
    pumpkin_seed_cost = 2.5
    tomato_seed_cost = 1.5
    chili_seed_cost = 0.9
    pumpkin_seed_quantity = 3
    tomato_seed_quantity = 4
    chili_seed_quantity = 5
    total_cost = (pumpkin_seed_cost * pumpkin_seed_quantity) + (tomato_seed_cost * tomato_seed_quantity) + (
                chili_seed_cost * chili_seed_quantity)
    result = total_cost
    return result

print(solution())