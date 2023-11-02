def solution():
    """Carmen needs $7 more to have twice the amount of money that Jethro has. Meanwhile, Patricia has $60, which is 3 times as much as Jethro. What is the sum of all their money?"""
    # Define the amount of money Patricia has
    patricia_money = 60

    # Calculate Jethro's money
    jethro_money = patricia_money / 3

    # Calculate Carmen's money
    carmen_money = jethro_money * 2 - 7

    # Calculate the sum of all their money
    sum_money = patricia_money + jethro_money + carmen_money

    # Display the sum of all their money
    result = sum_money
    return result

print(solution())