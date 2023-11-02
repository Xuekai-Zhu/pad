def solution():
    # growth rate for each year
    growth_rates = [2, 1.5, 1.5, 2, 0.5]

    # calculate height after each year
    height = 0
    for i in range(5):
        height += growth_rates[i] * 2
        # update growth rate for next year
        growth_rates[i+1] *= growth_rates[i] 

    return height

The tree will be 20 feet tall when it is 5 years old.

print(solution())