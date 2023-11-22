def solution():
    
    # Define the prices of each type of bike
    MTB_PRICE = 500
    BMX_PRICE = MTB_PRICE / 2
    Trekking_PRICE = 450
    BMX_Bike_PRICE = 0.15 * MTB_PRICE

    # Calculate the total number of bikes sold
    total_bikes = 300

    # Calculate the number of bikes sold for each type
    trekking_bikes = total_bikes / 2
    bMX_bikes = total_bikes * BMX_Bike_PRICE

    # Calculate the number of bikes sold for each type
    MTB_bikes = total_bikes - trekking_bikes - bMX_bikes
    BMX_bikes = total_bikes * BMX_Bike_PRICE

    # Calculate the total cost of the bikes sold for all types
    total_cost = trekking_bikes + BMX_bikes + MTB_

print(solution())