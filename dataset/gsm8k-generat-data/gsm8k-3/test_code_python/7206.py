def solution():
    """Yvonne brings a box of chocolates to school. Half have nuts and half do not. The students eat 80% of the ones with nuts and eat half of the ones without nuts. If there are 28 chocolates left, how many chocolates were in the box?"""
    # Define the total number of chocolates
    total_chocolates = 0

    # Define the number of chocolates with nuts and without nuts
    chocolates_with_nuts = 0
    chocolates_without_nuts = 0

    # Calculate the number of chocolates with nuts and without nuts
    chocolates_with_nuts = total_chocolates / 2
    chocolates_without_nuts = total_chocolates / 2

    # Calculate the number of chocolates eaten
    eaten_chocolates = chocolates_with_nuts * 0.8 + chocolates_without_nuts / 2

    # Calculate the number of chocolates remaining
    remaining_chocolates = total_chocolates - eaten_chocolates

    # Use the remaining chocolates to solve for the total number of chocolates
    total_chocolates = remaining_chocolates / 0.2

    # Display the total number of chocolates
    result = total_chocolates
    return result

print(solution())