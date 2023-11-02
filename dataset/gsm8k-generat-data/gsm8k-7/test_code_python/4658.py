def solution():
    total_money = 343
    num_brothers = 2
    each_share = total_money * (1/7)

    # Calculate the total amount given to Toby's brothers
    total_given = each_share * num_brothers

    # Calculate the remaining amount for Toby
    remaining_money = total_money - total_given
    result = remaining_money
    return result

print(solution())