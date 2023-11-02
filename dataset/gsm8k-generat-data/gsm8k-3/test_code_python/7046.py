def solution():
    """Jan collected 65 gallons of water in a barrel outside her home. She uses 7 gallons of water each to clean the two cars and uses 11 fewer gallons than the two cars to water the plants. Then, she uses half of the remaining gallons of water to wash the plates and clothes. How many gallons of water does Jan use to wash her plates and clothes?"""
    # Define the number of gallons of water used to clean the cars and water the plants
    CAR_GALLONS = 7
    PLANT_GALLONS = 2 * CAR_GALLONS - 11

    # Calculate the total number of gallons of water used for the cars and plants
    total_used = 2 * CAR_GALLONS + PLANT_GALLONS

    # Calculate the remaining number of gallons of water
    remaining_gallons = 65 - total_used

    # Calculate the number of gallons of water used to wash plates and clothes
    wash_gallons = remaining_gallons / 2

    # Display the number of gallons of water used to wash plates and clothes
    result = wash_gallons
    return result

print(solution())