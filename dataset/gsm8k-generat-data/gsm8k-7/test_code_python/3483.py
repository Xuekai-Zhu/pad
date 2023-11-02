def solution():
    num_households_per_day = 20
    num_days = 5
    percent_households_giving = 0.5
    num_twenty_dollar_bills = 2

    # Calculate the total number of households that Mark visited
    total_households_visited = num_households_per_day * num_days

    # Calculate the number of households that gave Mark a pair of 20s
    num_twenty_dollar_hh = total_households_visited * percent_households_giving

    # Calculate the total number of twenty dollar bills that Mark received
    total_twenty_dollar_bills = num_twenty_dollar_hh * num_twenty_dollar_bills

    # Calculate the total amount of money that Mark collected
    total_money_collected = total_twenty_dollar_bills * 20
    result = total_money_collected
    return result

print(solution())