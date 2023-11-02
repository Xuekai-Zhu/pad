def solution():
    """Carmen needs $7 more to have twice the amount of money that Jethro has. Meanwhile, Patricia has $60, which is 3 times as much as Jethro. What is the sum of all their money?"""
    # Define the amount of money Jethro has
    jethro_money = 60 / 3

    # Calculate the amount of money Carmen needs to have twice Jethro's money
    carmen_money = jethro_money * 2 - 7

    # Calculate the sum of all their money
    total_money = jethro_money + carmen_money + 60

    # return the result
    result = total_money
    return result

print(solution())