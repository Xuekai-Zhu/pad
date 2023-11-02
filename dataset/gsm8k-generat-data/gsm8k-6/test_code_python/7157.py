def solution():
    # Calculate the total number of apples gathered today
    total_apples = 6 * 240 * 5  # each farmhand can pick 240 apples per hour and will work 5 hours today
    golden_apples = (1/3) * total_apples  # ratio of golden delicious apples to pink lady apples is 1:2
    pink_apples = (2/3) * total_apples

    # Calculate the total number of pints of cider that can be made
    total_pints = min(golden_apples // 20, pink_apples // 40)  # it takes 20 golden delicious apples and 40 pink lady apples to make one pint of cider
    result = total_pints
    return result

print(solution())