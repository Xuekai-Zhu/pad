def solution():
    karen_quarters = 32  # Karen has 32 quarters
    christopher_quarters = 64  # Christopher has 64 quarters

    # Calculate the difference in the number of quarters between Karen and Christopher
    difference_quarters = christopher_quarters - karen_quarters

    # Calculate the difference in the amount of money between Karen and Christopher
    difference_money = difference_quarters * 0.25

    result = difference_money
    return result

print(solution())