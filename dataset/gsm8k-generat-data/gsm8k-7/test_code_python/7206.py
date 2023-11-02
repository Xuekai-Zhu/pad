def solution():
    num_chocolates = 0
    num_chocolates_with_nuts = num_chocolates / 2
    num_chocolates_without_nuts = num_chocolates / 2

    # Calculate the number of chocolates with nuts that were eaten
    num_chocolates_with_nuts_eaten = 0.8 * num_chocolates_with_nuts

    # Calculate the number of chocolates without nuts that were eaten
    num_chocolates_without_nuts_eaten = 0.5 * num_chocolates_without_nuts

    # Calculate the total number of chocolates eaten
    num_chocolates_eaten = num_chocolates_with_nuts_eaten + num_chocolates_without_nuts_eaten

    # Calculate the number of chocolates left
    num_chocolates_left = 28

    # Calculate the original number of chocolates in the box
    num_chocolates = num_chocolates_left + num_chocolates_eaten
    result = num_chocolates
    return result

print(solution())