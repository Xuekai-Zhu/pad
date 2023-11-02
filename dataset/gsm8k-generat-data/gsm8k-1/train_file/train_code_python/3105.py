def solution():
    """Marta sells tomatoes in a grocery store. On Friday, a shipment of 1000 kg of tomatoes arrived at the store. On Saturday, Marta sold a total of 300 kg of tomatoes to customers. On Sunday, the store was closed, causing 200 kg of tomatoes to rot and to be thrown away. On Monday morning another shipment arrived, twice the size of the first one. How many kilograms of tomatoes did Marta have ready for sale on Tuesday?"""
    initial_shipment = 1000
    sold_saturday = 300
    rotten_sunday = 200
    second_shipment = initial_shipment * 2
    total_tomatoes = initial_shipment - sold_saturday - rotten_sunday + second_shipment
    result = total_tomatoes
    return result

print(solution())