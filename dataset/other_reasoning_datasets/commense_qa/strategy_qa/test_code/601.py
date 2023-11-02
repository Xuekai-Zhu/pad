def solution():
    harvey_milk_elected = True
    harvey_milk_assassinated = True
    harvey_milk_ran_for_governor = False
    if harvey_milk_elected and harvey_milk_assassinated and not harvey_milk_ran_for_governor:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())