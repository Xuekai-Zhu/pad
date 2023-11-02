def solution():
    # Calculate the total amount earned from selling shirts
    shirt_sales = 5 * 1

    # Calculate the total amount earned from selling pants
    pant_sales = 5 * 3

    # Calculate the total amount earned from selling clothes
    total_sales = shirt_sales + pant_sales

    # Calculate the amount Kekai gives to his parents
    parents_share = total_sales / 2

    # Calculate the amount Kekai has left
    remaining_money = total_sales - parents_share
    result = remaining_money
    return result

print(solution())