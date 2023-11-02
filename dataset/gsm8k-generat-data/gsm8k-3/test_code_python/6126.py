def solution():
    """Paul makes pencils, making 100 pencils a day five days a week. He started the week with 80 pencils in his stock, and during the week he sold 350 pencils. How many pencils did he have in his stock at the end of the week?"""
    # Define the number of pencils made per week
    pencils_made = 100 * 5

    # Calculate the total number of pencils at the beginning of the week
    beginning_stock = 80

    # Calculate the total number of pencils sold during the week
    pencils_sold = 350

    # Calculate the total number of pencils at the end of the week
    ending_stock = beginning_stock + pencils_made - pencils_sold

    # Display the total number of pencils at the end of the week
    result = ending_stock
    return result

print(solution())