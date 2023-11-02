def solution():
    num_hiphop_classes = 2
    hiphop_price = 10

    num_ballet_classes = 2
    ballet_price = 12

    num_jazz_classes = 1
    jazz_price = 8

    # Calculate the total cost of hip-hop classes
    total_hiphop_cost = num_hiphop_classes * hiphop_price

    # Calculate the total cost of ballet classes
    total_ballet_cost = num_ballet_classes * ballet_price

    # Calculate the total cost of jazz class
    total_jazz_cost = num_jazz_classes * jazz_price

    # Calculate the total cost of all dance classes
    total_cost = total_hiphop_cost + total_ballet_cost + total_jazz_cost
    result = total_cost
    return result

print(solution())