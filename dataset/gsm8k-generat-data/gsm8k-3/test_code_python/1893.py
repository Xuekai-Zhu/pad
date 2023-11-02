def solution():
    """James gets paid $0.50/mile to drive a truck carrying hazardous waste. He has to pay $4.00/gallon for gas and his truck gets 20 miles per gallon. How much profit does he make from a 600 mile trip?"""
    # Define the payment rate per mile and the gas cost per gallon
    PAYMENT_RATE = 0.5
    GAS_COST = 4.0

    # Define the distance of the trip and the truck's gas mileage
    DISTANCE = 600
    GAS_MILEAGE = 20

    # Calculate the amount of gas needed for the trip
    gas_needed = DISTANCE / GAS_MILEAGE

    # Calculate the total cost of gas for the trip
    gas_cost = gas_needed * GAS_COST

    # Calculate James' earnings for the trip
    earnings = DISTANCE * PAYMENT_RATE

    # Calculate James' profit for the trip
    profit = earnings - gas_cost

    # Display James' profit
    result = profit
    return result

print(solution())