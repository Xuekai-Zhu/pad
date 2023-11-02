def solution():
    # Number of times she cuts her lawn each month
    march_apr_sep_oct = 2
    may_june_july_aug = 4

    # Number of times she needs to cut her lawn from March through October
    total_cutting_times = (march_apr_sep_oct * 4) + (may_june_july_aug * 4)

    # Number of times she needs to use gas
    gas_cutting_times = total_cutting_times // 4

    # Number of gallons of gas needed
    gallons_of_gas = gas_cutting_times * 2

    result = gallons_of_gas
    return result

print(solution())