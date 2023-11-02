def solution():
    whole_foods_cost = 1.1 # We assume this means Whole Foods costs 10% more than other stores
    aldi_discount = 0.8 # We assume this means Aldi has a 20% discount
    if aldi_discount < whole_foods_cost:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())