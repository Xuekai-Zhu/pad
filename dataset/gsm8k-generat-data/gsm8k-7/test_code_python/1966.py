def solution():
    pants_price = 5
    num_pants = 3
    shorts_price = 3
    num_shorts = 5
    shirt_price = 4

    # Calculate the total amount of money Selina made from selling pants and shorts
    total_pants_money = pants_price * num_pants
    total_shorts_money = shorts_price * num_shorts
    total_clothing_money = total_pants_money + total_shorts_money

    # Calculate the total number of shirts sold
    total_shirts_sold = int((30 - 2*10 - total_clothing_money) / shirt_price)
    result = total_shirts_sold
    return result

print(solution())