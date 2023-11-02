def solution():
    # Calculate the cost of the pack of 10 classes
    pack_cost = 75  

    # Calculate the average price per class in the pack
    avg_price_pack = pack_cost / 10  

    # Calculate the cost of an additional class (1/3 more than the average price)
    extra_class_cost = avg_price_pack * (1 + 1/3)  

    # Calculate the total cost for 13 classes (10 in the pack, 3 additional)
    total_cost = pack_cost + (3 * extra_class_cost)
    result = total_cost
    return result

print(solution())