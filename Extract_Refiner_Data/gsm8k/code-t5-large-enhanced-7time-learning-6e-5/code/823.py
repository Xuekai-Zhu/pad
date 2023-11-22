def solution():
    
    book_weight = 4
    book_price = 32
    distance_to_center = 20
    shipping_price_per_pound = 0.35
    shipping_price_per_mile = 0.08
    amazon_refund_percent = 75
    
    # calculate the total distance to be returned
    total_distance = distance_to_center * 2
    
    # calculate the total cost of the book
    total_cost = book_price + (total_distance * shipping_price_per_pound)
    
    # calculate the amount of money Amazon will lose
    amazon_loss = total_cost * (1 - amazon_refund_percent/100)
    
    result = amazon_loss
    return result

print(solution())