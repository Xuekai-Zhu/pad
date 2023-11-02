def solution():
    """Marta sells tomatoes in a grocery store. On Friday, a shipment of 1000 kg of tomatoes arrived at the store. On Saturday, Marta sold a total of 300 kg of tomatoes to customers. On Sunday, the store was closed, causing 200 kg of tomatoes to rot and to be thrown away. On Monday morning another shipment arrived, twice the size of the first one. How many kilograms of tomatoes did Marta have ready for sale on Tuesday?"""
    # Define the initial amount of tomatoes
    initial_tomatoes = 1000

    # Calculate the amount of tomatoes remaining after Saturday's sales
    remaining_tomatoes = initial_tomatoes - 300

    # Calculate the amount of tomatoes remaining after Sunday's waste
    remaining_tomatoes -= 200

    # Calculate the amount of tomatoes in Monday's shipment
    monday_shipment = initial_tomatoes * 2

    # Calculate the total amount of tomatoes Marta had on Tuesday
    total_tomatoes = remaining_tomatoes + monday_shipment

    # Return the result
    result = total_tomatoes
    return result

print(solution())