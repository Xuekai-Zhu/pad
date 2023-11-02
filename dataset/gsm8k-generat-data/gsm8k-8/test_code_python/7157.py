def solution():
    # Calculate the total number of apples gathered
    total_apples = 6 * 240 * 5

    # Calculate the number of golden delicious apples gathered
    golden_delicious_apples = (1/3) * total_apples

    # Calculate the number of pink lady apples gathered
    pink_lady_apples = (2/3) * total_apples

    # Calculate the number of pints of cider that can be made
    pints_of_cider = min(golden_delicious_apples/20, pink_lady_apples/40)

    result = pints_of_cider
    return result

print(solution())