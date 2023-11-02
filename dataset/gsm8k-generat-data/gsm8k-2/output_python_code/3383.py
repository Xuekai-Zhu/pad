def solution():
    """The doctor told Barry to take vitamin D3 for 180 days to help protect him from infections. The pharmacy only sold vitamin D3 in bottles containing 60 capsules, with a daily serving size of 2 capsules. How many bottles would Barry need to buy to have enough servings to last for 180 days?"""
    total_days = 180
    capsules_per_serv = 2
    capsules_per_bottle = 60
    total_servings = total_days * capsules_per_serv
    total_bottles = total_servings // capsules_per_bottle
    if total_servings % capsules_per_bottle != 0:
        total_bottles += 1
    result = total_bottles
    return result

print(solution())