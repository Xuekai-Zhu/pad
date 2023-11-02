def solution():
    # Let's assume there are 'x' chocolates in the box
    x = 0

    # Calculate the number of chocolates with nuts and without nuts
    chocolates_with_nuts = x / 2
    chocolates_without_nuts = x / 2

    # Calculate the number of chocolates eaten
    chocolates_eaten = 0.8 * chocolates_with_nuts + 0.5 * chocolates_without_nuts

    # Calculate the number of chocolates left
    chocolates_left = x - chocolates_eaten

    # Given that there are 28 chocolates left, we can solve for 'x'
    x = chocolates_left / 0.5

    result = x
    return result

print(solution())