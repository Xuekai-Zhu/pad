def solution():
    """One dwarf can mine 12 pounds of ore per day with his bare hands. He can mine twice as much with an iron pickaxe and 50% more with a steel pickaxe than with an iron pickaxe. How many pounds of ore can 40 dwarves with steel pickaxes mine in a month with 30 days?"""
    dwarves = 40
    days = 30
    bare_hand_mining_rate = 12
    iron_pickaxe_mining_rate = bare_hand_mining_rate * 2
    steel_pickaxe_mining_rate = iron_pickaxe_mining_rate * 1.5
    total_mining_rate = dwarves * steel_pickaxe_mining_rate
    total_mined = total_mining_rate * days
    result = total_mined
    return result

print(solution())