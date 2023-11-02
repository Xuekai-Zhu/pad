def solution():
    # Calculate the amount of money Benny added in February
    feb_money = 19

    # Calculate the total amount of money in the piggy bank after February
    feb_total = 19 + feb_money  

    # Calculate the amount of money Benny added in March
    mar_money = 46 - feb_total

    result = mar_money
    return result

print(solution())