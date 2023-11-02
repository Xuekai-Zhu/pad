def solution():
    """Yvonne brings a box of chocolates to school. Half have nuts and half do not. The students eat 80% of the ones with nuts and eat half of the ones without nuts. If there are 28 chocolates left, how many chocolates were in the box?"""
    # Define the initial number of chocolates
    chocolates = None

    chocolates_final = 28

    # Calculate the number of chocolates with nuts
    chocolates_nuts = chocolates_final * 0.4

    # Calculate the number of chocolates without nuts
    chocolates_no_nuts = chocolates_final * 0.6
    chocolates_no_nuts = chocolates_no_nuts * 0.5

    chocolates = chocolates_nuts + chocolates_no_nuts

    result = chocolates
    return result

print(solution())