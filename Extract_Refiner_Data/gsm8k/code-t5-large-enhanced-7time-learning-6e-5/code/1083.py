def solution():
    
    # Define the number of hours the farmer and the truck driver put in the day
    HOURS_PER_DAY = 6

    # Define the number of bales made by the farmer and the truck each hour
    FIRMER_BALLS = 5
    TRUCK_BALLS = 3

    # Calculate the total number of bales made by the farmer and the truck
    total_bales = (FIRMER_BALLS + TRUCK_BALLS) * HOURS_PER_DAY

    # Calculate the number of bales left in the field
    bales_left = total_bales - (FIRMER_BALLS + TRUCK_BALLS)

    # Display the number of bales left in the field
    result = bales_left
    return result

print(solution())