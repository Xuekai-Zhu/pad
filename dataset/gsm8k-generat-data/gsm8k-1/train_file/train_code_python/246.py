def solution():
    """Tony has a terrible toothache and decides to buy some painkillers from the store. He picks up a bottle of 50 pills and takes them home. He takes 2 pills each day three times a day for the first 2 days, before cutting this amount in half for the next 3 days. On the sixth day, he takes a final 2 pills in the morning and ends up feeling better. How many pills are left in the bottle?"""
    pills_per_bottle = 50
    total_pills_used = (2 * 3 * 2) + ((2 / 2) * 3 * 3) + 2
    pills_left = pills_per_bottle - total_pills_used
    result = pills_left
    return result

print(solution())