def solution():
    # Calculate the total weight of the apples sold
    weight_sold = 405 - 90 - 60  # subtract the weight used for fruit juice and given to a restaurant
    # Calculate the total number of 5 kg bags sold
    bags_sold = weight_sold / 5
    # Calculate the selling price of one bag of apples
    price_per_bag = 408 / bags_sold
    result = price_per_bag
    return result

print(solution())