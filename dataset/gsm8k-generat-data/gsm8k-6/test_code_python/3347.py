def solution():
    # Calculate the total number of stuffed animals Trish has
    num_Trish_animals = 2 * 9

    # Calculate the total amount of money Barbara will earn for selling her stuffed animals
    money_Barbara = 9 * 2

    # Calculate the total amount of money Trish will earn for selling her stuffed animals
    money_Trish = num_Trish_animals * 1.5

    # Calculate the total amount of money they will donate to their class funds
    total_money = money_Barbara + money_Trish
    result = total_money
    return result

print(solution())