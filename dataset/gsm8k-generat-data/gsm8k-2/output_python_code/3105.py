def solution():
    """Marta sells tomatoes in a grocery store. On Friday, a shipment of 1000 kg of tomatoes arrived at the store. On Saturday, Marta sold a total of 300 kg of tomatoes to customers. On Sunday, the store was closed, causing 200 kg of tomatoes to rot and to be thrown away. On Monday morning another shipment arrived, twice the size of the first one. How many kilograms of tomatoes did Marta have ready for sale on Tuesday?"""
    friday_shipment = 1000
    saturday_sales = 300
    sunday_waste = 200
    monday_shipment = 2 * friday_shipment
    total_tomatoes = friday_shipment - saturday_sales - sunday_waste + monday_shipment
    result = total_tomatoes
    return result

print(solution())