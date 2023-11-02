def solution():
    total_apples = 405  # Total weight of harvested apples
    juice_apples = 90  # Weight of apples used for fruit juice
    restaurant_apples = 60  # Weight of apples given to a restaurant
    sold_apples = total_apples - juice_apples - restaurant_apples  # Weight of apples sold in 5 kg bags
    bags_sold = sold_apples / 5  # Number of bags of apples sold
    total_sale = 408  # Total revenue from selling bags of apples

    # Calculate the selling price of one bag of apples
    price_per_bag = total_sale / bags_sold
    result = price_per_bag
    return result

print(solution())