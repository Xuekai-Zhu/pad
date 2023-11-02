def solution():
    # Define the variables
    total_money = 67
    ali_money = 0
    nada_money = 0
    john_money = 0

    # Calculate Ali's money using the given information
    ali_money = nada_money - 5

    # Calculate John's money using the given information
    john_money = 4 * nada_money

    # Calculate Nada's money by subtracting Ali and John's money from the total
    nada_money = (total_money - ali_money - john_money) / 2

    # Return John's money as the result
    result = john_money
    return result

print(solution())