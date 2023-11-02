def solution():
    """At Clark's Food Store, apples cost 40 dollars for a dozen, and pears cost 50 dollars for a dozen. If Hank bought 14 dozen of each kind of fruit, how many dollars did he spend?"""
    apples_cost = 40
    pears_cost = 50
    dozen_in_order = 14
    total_apples_cost = apples_cost * dozen_in_order
    total_pears_cost = pears_cost * dozen_in_order
    total_cost = total_apples_cost + total_pears_cost
    result = total_cost
    return result

print(solution())