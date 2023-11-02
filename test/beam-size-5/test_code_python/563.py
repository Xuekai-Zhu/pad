def solution():
    
    # Define the initial amount of money the tooth fairy lost
    initial_money = 5

    # Define the amount of money the tooth fairy gave to the first three teeth Sharon
    first_three_money = 1

    # Define the amount of money the tooth fairy gave to the second two teeth Sharon
    second_three_money = 1

    # Define the amount of money the tooth fairy gave to the third three teeth Sharon
    third_three_money = (first_three_money + second_three_money) / 2

    # Calculate the total amount of money the tooth fairy gave to Sharon
    total_money = initial_money + second_three_money + third_three_money

    # return the result
    result = total_money
    return result

print(solution())