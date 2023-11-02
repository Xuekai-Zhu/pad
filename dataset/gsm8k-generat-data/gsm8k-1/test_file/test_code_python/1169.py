def solution():
    """A regular box of 100 dishwasher pods costs $12. There's currently a special size box for the same price that has 20% more pods. How many dishwashing cycles with the new box can you run for $1 if you use 1 pod per cycle?"""
    regular_pods = 100
    regular_price = 12
    special_pods = regular_pods * 1.2
    special_price = regular_price
    pods_per_dollar = special_pods / special_price
    cycles_per_pod = 1
    cycles_per_dollar = cycles_per_pod * pods_per_dollar
    result = cycles_per_dollar
    return result

print(solution())