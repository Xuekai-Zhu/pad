def solution():
    # Calculate the total value of the $10 bills
    value_of_tens = 10 * 10  # Ten $10 bills

    # Calculate the total value of the $5 bills
    number_of_fives = 10 - 4  # Four fewer $5 bills than $10 bills
    value_of_fives = number_of_fives * 5

    # Calculate the total value of Shelly's money
    total_value = value_of_tens + value_of_fives
    result = total_value
    return result

print(solution())