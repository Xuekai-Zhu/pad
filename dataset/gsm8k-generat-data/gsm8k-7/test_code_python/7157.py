def solution():
    num_golden_apples_per_pint = 20
    num_pink_apples_per_pint = 40
    num_farmhands = 6
    apples_per_hour_per_farmhand = 240
    work_hours = 5

    # Calculate the total number of apples gathered today
    total_apples = num_farmhands * apples_per_hour_per_farmhand * work_hours

    # Calculate the number of golden delicious apples gathered today based on the 1:2 ratio
    num_golden_apples = total_apples // 3

    # Calculate the number of pink lady apples gathered today based on the 1:2 ratio
    num_pink_apples = 2 * num_golden_apples

    # Calculate the total number of pints of cider that can be made with the apples gathered today
    num_pints = min(num_golden_apples // num_golden_apples_per_pint, num_pink_apples // num_pink_apples_per_pint)
    result = num_pints
    return result

print(solution())