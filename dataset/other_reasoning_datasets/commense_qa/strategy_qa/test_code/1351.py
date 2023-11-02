def solution():
    bill_gates_birth_year = 1955
    jeff_bezos_birth_year = 1964
    baby_boomer_start_year = 1946
    baby_boomer_end_year = 1964
    if bill_gates_birth_year >= baby_boomer_start_year and bill_gates_birth_year <= baby_boomer_end_year:
        bill_gates_is_boomer = True
    else:
        bill_gates_is_boomer = False
    if jeff_bezos_birth_year >= baby_boomer_start_year and jeff_bezos_birth_year <= baby_boomer_end_year:
        jeff_bezos_is_boomer = True
    else:
        jeff_bezos_is_boomer = False
    if bill_gates_is_boomer and not jeff_bezos_is_boomer:
        result = "yes"
    elif not bill_gates_is_boomer and jeff_bezos_is_boomer:
        result = "no"
    elif bill_gates_is_boomer and jeff_bezos_is_boomer:
        if bill_gates_net_worth > jeff_bezos_net_worth:
            result = "yes"
        else:
            result = "no"
    else:
        result = "neither"
    return result

print(solution())