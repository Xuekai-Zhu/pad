def solution():
    """There are 30 spaces for each vehicle in a parking lot. A caravan takes up a total of 2 spaces of parking space. How many vehicles can still park if there are 3 caravans currently parking?"""
    # Define the number of parking spaces in the lot and the number of spaces taken up by each caravan
    PARKING_SPACES = 30
    CARAVAN_SPACES = 2

    # Calculate the total number of parking spaces taken up by the caravans
    total_caravan_spaces = 3 * CARAVAN_SPACES

    # Calculate the number of parking spaces remaining for vehicles
    remaining_spaces = PARKING_SPACES * 3 - total_caravan_spaces

    # Calculate the number of vehicles that can still park
    vehicles_parking = remaining_spaces // PARKING_SPACES

    # Display the number of vehicles that can still park
    result = vehicles_parking
    return result

print(solution())