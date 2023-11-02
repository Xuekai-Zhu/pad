def solution():
    
    num_shirts = 2
    shirt_price = 7
    shoe_price = shirt_price + 3
    bag_price = (num_shirts * shirt_price + shoe_price) / 2
    total_price = num_shirts * shirt_price + shoe_price + bag_price
    result = total_price
    return result

print(solution())