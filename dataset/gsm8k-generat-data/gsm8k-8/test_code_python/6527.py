def solution():
    # Define the initial amount of money Cathy has
    initial_money = 12

    # Define the amount of money Cathy's dad sent her
    dad_money = 25

    # Define the amount of money Cathy's mom sent her
    mom_money = 2 * dad_money

    # Calculate the total amount of money Cathy has now
    total_money = initial_money + dad_money + mom_money
    result = total_money
    return result

print(solution())