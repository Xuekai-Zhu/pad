def solution():
    """Tony has a terrible toothache and decides to buy some painkillers from the store. He picks up a bottle of 50 pills and takes them home. He takes 2 pills each day three times a day for the first 2 days, before cutting this amount in half for the next 3 days. On the sixth day, he takes a final 2 pills in the morning and ends up feeling better. How many pills are left in the bottle?"""
    pills_per_day = 2
    pills_per_dose = 3
    days = 2
    pills_left = pills_per_day * pills_per_dose * days
    result = pills_left
    return result

print(solution())