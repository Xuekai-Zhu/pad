def solution():
    # Calculate the amount earned from selling shirts
    shirts_sold = 5
    price_per_shirt = 1
    total_shirt_sale = shirts_sold * price_per_shirt

    # Calculate the amount earned from selling pants
    pants_sold = 5
    price_per_pant = 3
    total_pant_sale = pants_sold * price_per_pant

    # Calculate the total amount earned from the garage sale
    total_sale = total_shirt_sale + total_pant_sale

    # Calculate the amount of money Kekai gives to his parents
    money_given_to_parents = total_sale / 2

    # Calculate the amount of money Kekai has left
    money_left = total_sale - money_given_to_parents
    result = money_left
    return result

print(solution())