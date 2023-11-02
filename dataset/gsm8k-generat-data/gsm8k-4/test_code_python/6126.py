def solution():
    """Paul makes pencils, making 100 pencils a day five days a week. He started the week with 80 pencils in his stock, and during the week he sold 350 pencils. How many pencils did he have in his stock at the end of the week?"""
    # Define the number of pencils made each week
    pencils_made = 100 * 5

    # Define the starting stock and the number of pencils sold
    starting_stock = 80
    pencils_sold = 350

    # Calculate the remaining stock at the end of the week
    remaining_stock = starting_stock + pencils_made - pencils_sold

    # Return the result
    result = remaining_stock
    return result

print(solution())