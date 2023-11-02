def solution():
    """Geordie takes a toll road on his drive to work and back every day of his five-day workweek. The toll is $12.50 per car or $7 per motorcycle. Both his car and his motorcycle get 35 miles per gallon of gas and the commute to work is 14 miles. Gas costs him $3.75 per gallon. Geordie drives his car to work three times a week and his motorcycle to work twice a week. How many dollars does he spend driving to work and back on the same route in a week?"""
    
    #Define the prices for the tolls
    CAR_TOLL = 12.50 
    MOTORCYCLE_TOLL = 7 
    
    #Define the mileage values 
    COMMUTE_MILEAGE = 14 #miles
    GAS_MILEAGE = 35 #miles/gallon
    GAS_PRICE = 3.75 #dollars/gallon
    
    #Calculate the total distance Geordie travels in a week
    total_distance = (COMMUTE_MILEAGE * 2) * 5 #2 trips per day, 5 days per week
    
    #Calculate the total gas used driving the car to work
    car_gas_used = (total_distance * 3) / GAS_MILEAGE #3 days per week driving car
    
    #Calculate the total gas used driving the motorcycle to work
    motorcycle_gas_used = (total_distance * 2) / GAS_MILEAGE #2 days per week driving motorcycle
    
    #Calculate the total cost of gas for the week
    total_gas_cost = (car_gas_used + motorcycle_gas_used) * GAS_PRICE
    
    #Calculate the total cost of tolls for the week
    total_toll_cost = (CAR_TOLL * 3) + (MOTORCYCLE_TOLL * 2) #3 days per week driving car, 2 days per week driving motorcycle
    
    #Calculate the total cost of driving to work and back in a week
    total_cost = total_gas_cost + total_toll_cost
    
    result = total_cost
    return result

print(solution())