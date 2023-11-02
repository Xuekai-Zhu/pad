def solution():
    """Marta sells tomatoes in a grocery store. On Friday, a shipment of 1000 kg of tomatoes arrived at the store. On Saturday, Marta sold a total of 300 kg of tomatoes to customers. On Sunday, the store was closed, causing 200 kg of tomatoes to rot and to be thrown away. On Monday morning another shipment arrived, twice the size of the first one. How many kilograms of tomatoes did Marta have ready for sale on Tuesday?"""
    # Define the initial shipment and the amount sold on Saturday and discarded on Sunday
    initial_shipment = 1000
    amount_sold = 300
    amount_discarded = 200

    # Calculate the amount of tomatoes remaining
    remaining_tomatoes = initial_shipment - amount_sold - amount_discarded

    # Calculate the size of the second shipment
    second_shipment = initial_shipment * 2

    # Calculate the total amount of tomatoes available on Tuesday
    total_tomatoes = remaining_tomatoes + second_shipment

    # Display the total amount of tomatoes
    result = total_tomatoes
    return result

print(solution())