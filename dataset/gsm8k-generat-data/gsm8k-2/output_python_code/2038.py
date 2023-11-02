def solution():
    """Leo had 400 marbles in a jar. He packed the marbles with ten marbles in each pack, and he gave some of them to his two friends, Manny and Neil. He gave Manny 1/4 of the number of packs of marbles, Neil received 1/8 of the number of packs of marbles, and he kept the rest. How many packs of marbles did Leo keep?"""
    total_packs = 400 / 10
    manny_packs = total_packs * (1/4)
    neil_packs = total_packs * (1/8)
    leo_packs = total_packs - manny_packs - neil_packs
    result = leo_packs
    return result

print(solution())