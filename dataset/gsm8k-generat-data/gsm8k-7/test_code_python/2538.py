def solution():
    ray_money = 175
    peter_money = 30
    randi_money = 2 * peter_money

    # Calculate the remaining money that Ray has after giving 30 cents to Peter
    remaining_money = ray_money - peter_money

    # Calculate the amount of money that Ray gives to Randi
    randi_money_given = randi_money - peter_money

    # Calculate the number of nickels that Ray has left
    remaining_nickels = remaining_money // 5

    # Calculate the number of nickels that Randi has
    randi_nickels = randi_money_given // 5

    # Calculate the number of nickels that Peter has
    peter_nickels = peter_money // 5

    # Calculate the difference in the number of nickels between Randi and Peter
    nickel_difference = randi_nickels - peter_nickels

    result = nickel_difference
    return result

print(solution())