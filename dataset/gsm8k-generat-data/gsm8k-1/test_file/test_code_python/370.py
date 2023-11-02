def solution():
    """Mary has 30 sheep. She gets 1 kg of milk from half of them and 2 kg of milk from the other half every day. How much milk does she collect every day?"""
    total_sheep = 30
    half_sheep = total_sheep / 2
    milk_one_half = half_sheep * 1
    milk_other_half = half_sheep * 2
    total_milk = milk_one_half + milk_other_half
    result = total_milk
    return result

print(solution())