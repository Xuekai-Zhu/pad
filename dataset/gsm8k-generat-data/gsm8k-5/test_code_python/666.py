def solution():
    total_money = 150  # Together, Jackson and Williams have $150
    jackson_ratio = 5  # Jackson has 5 times more money than Williams

    # Calculate the total ratio of Jackson's money to Williams' money
    total_ratio = jackson_ratio + 1  # Add 1 to account for Williams' money

    # Calculate the amount of money Jackson has
    jackson_money = (jackson_ratio / total_ratio) * total_money

    result = jackson_money
    return result

print(solution())