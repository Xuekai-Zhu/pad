def solution():
    shipment_1 = 1000
    sold_1 = 300
    rotten_1 = 200
    shipment_2 = shipment_1 * 2
    total_tomatoes = shipment_1 + shipment_2 - sold_1 - rotten_1
    result = total_tomatoes
    return result

print(solution())