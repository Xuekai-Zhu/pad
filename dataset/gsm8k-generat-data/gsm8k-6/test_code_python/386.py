def solution():
    # Calculate the discount and the new price of the shoes
    shoe_discount = 0.4 * 50  # 40 percent off on $50 shoes
    new_shoe_price = 50 - shoe_discount
    total_shoe_price = new_shoe_price * 2  # Daniela buys 2 pairs of shoes

    # Calculate the discount and the new price of the dress
    dress_discount = 0.2 * 100  # 20 percent off on $100 dress
    new_dress_price = 100 - dress_discount

    # Calculate the total amount Daniela spends
    total_spent = total_shoe_price + new_dress_price
    result = total_spent
    return result

print(solution())