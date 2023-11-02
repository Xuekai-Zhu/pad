def solution():
    
    cherries_price = 5
    olives_price = 7
    num_bags = 50
    total_price = (cherries_price + olives_price) * num_bags
    discount = 0.1 * total_price
    final_price = total_price - discount
    result = final_price
    return result

print(solution())