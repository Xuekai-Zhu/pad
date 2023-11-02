def solution():
    
    initial_shipment = 1000
    sold_saturday = 300
    rotten_sunday = 200
    second_shipment = initial_shipment * 2
    total_tomatoes = initial_shipment - sold_saturday - rotten_sunday + second_shipment
    result = total_tomatoes
    return result

print(solution())