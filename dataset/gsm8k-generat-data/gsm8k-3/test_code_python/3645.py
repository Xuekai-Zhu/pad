def solution():
    """Geordie takes a toll road on his drive to work and back every day of his five-day workweek. The toll is $12.50 per car or $7 per motorcycle. Both his car and his motorcycle get 35 miles per gallon of gas and the commute to work is 14 miles. Gas costs him $3.75 per gallon. Geordie drives his car to work three times a week and his motorcycle to work twice a week. How many dollars does he spend driving to work and back on the same route in a week?"""
    # Define the cost of tolls and gas
    CAR_TOLL = 12.5
    MOTORCYCLE_TOLL = 7
    GAS_PRICE = 3.75

    # Define Geordie's commute distance
    COMMUTE_DISTANCE = 14

    # Define Geordie's vehicle gas mileage
    GAS_MILEAGE = 35

    # Define the number of car and motorcycle commutes per week
    CAR_COMMUTES = 3
    MOTORCYCLE_COMMUTES = 2

    # Calculate the amount of gas Geordie uses per car commute
    car_gas_used = (2 * COMMUTE_DISTANCE) / GAS_MILEAGE

    # Calculate the amount of gas Geordie uses per motorcycle commute
    motorcycle_gas_used = (2 * COMMUTE_DISTANCE) / GAS_MILEAGE

    # Calculate Geordie's total gas cost for the week
    total_gas_cost = (CAR_COMMUTES * car_gas_used + MOTORCYCLE_COMMUTES * motorcycle_gas_used) * GAS_PRICE

    # Calculate Geordie's total toll cost for the week
    total_toll_cost = CAR_COMMUTES * CAR_TOLL + MOTORCYCLE_COMMUTES * MOTORCYCLE_TOLL

    # Calculate Geordie's total cost for the week
    total_cost = total_gas_cost + total_toll_cost

    # Display Geordie's total cost for the week
    result = total_cost
    return result

print(solution())