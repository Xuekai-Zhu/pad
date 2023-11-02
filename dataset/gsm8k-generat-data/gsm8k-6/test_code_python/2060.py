def solution():
    total_milk = 16  # cups of milk provided by Daisy's cow per day
    consumed_by_kids = 0.75 * total_milk  # cups of milk consumed by Daisy's kids
    remaining_milk_1 = total_milk - consumed_by_kids  # remaining milk after kids consume their share
    used_for_cooking = 0.5 * remaining_milk_1  # cups of milk used for cooking
    remaining_milk_2 = remaining_milk_1 - used_for_cooking  # remaining milk after some is used for cooking
    result = remaining_milk_2
    return result

print(solution())