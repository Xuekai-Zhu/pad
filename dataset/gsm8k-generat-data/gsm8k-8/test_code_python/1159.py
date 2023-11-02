def solution():
    # Calculate the discounted price of the shoes
    shoe_price = 200
    shoe_discount = 0.3
    discounted_shoe_price = shoe_price - (shoe_price * shoe_discount)

    # Calculate the total price of the shirts
    shirt_price = 80
    num_shirts = 2
    total_shirt_price = shirt_price * num_shirts

    # Calculate the total price before additional discount
    total_price = discounted_shoe_price + total_shirt_price

    # Calculate the final price after additional discount
    additional_discount = 0.05
    final_price = total_price - (total_price * additional_discount)

    result = final_price
    return result

print(solution())