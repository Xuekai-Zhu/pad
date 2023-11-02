def solution():
    initial_money = 200
    percent_increase = 0.2

    # Calculate the amount of money that Susie will add to her piggy bank
    increase_amount = initial_money * percent_increase

    # Calculate the total amount of money that Susie will have after the increase
    total_money = initial_money + increase_amount
    result = total_money
    return result

print(solution())