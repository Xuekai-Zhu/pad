def solution():
    eggs_per_year = 30
    infertile_percent = 0.2
    calcification_percent = 1/3

    # Calculate the number of infertile eggs
    num_infertile = round(eggs_per_year * infertile_percent)

    # Calculate the number of fertile eggs
    num_fertile = eggs_per_year - num_infertile

    # Calculate the number of eggs that will not hatch due to calcification issues
    num_calcified = round(num_fertile * calcification_percent)

    # Calculate the number of eggs that will actually hatch
    num_hatched = num_fertile - num_calcified
    result = num_hatched
    return result

print(solution())