def solution():
    # Find the cost of Pauline's dress
    paulines_dress = 30

    # Find the cost of Jean's dress
    jeans_dress = paulines_dress - 10

    # Find the cost of Ida's dress
    idas_dress = jeans_dress + 30

    # Find the cost of Patty's dress
    pattys_dress = idas_dress + 10

    # Find the total cost of all the dresses
    total_cost = paulines_dress + jeans_dress + idas_dress + pattys_dress
    result = total_cost
    return result

print(solution())