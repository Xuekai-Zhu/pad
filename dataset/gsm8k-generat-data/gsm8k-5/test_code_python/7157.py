def solution():
    # Calculate the total number of apples gathered
    total_apples = 6 * 240 * 5  # 6 farmhands, 240 apples per hour, 5 hours

    # Calculate the number of golden delicious apples gathered (assuming a 1:2 ratio)
    num_golden_delicious = total_apples // 3
    num_pink_lady = 2 * num_golden_delicious  # 1:2 ratio

    # Calculate the number of pints of cider that can be made
    num_pints = min(num_golden_delicious // 20, num_pink_lady // 40)

    result = num_pints
    return result

print(solution())