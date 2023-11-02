def solution():
    """The Dark Lord needs to transport 1200 pounds of swords to the Enchanted Forest for a battle with the elves. He has 10 squads of 8 orcs each. How many pounds of swords does each orc have to carry?"""
    total_weight = 1200
    num_orcs = 10 * 8
    weight_per_orc = total_weight / num_orcs
    result = weight_per_orc
    return result

print(solution())