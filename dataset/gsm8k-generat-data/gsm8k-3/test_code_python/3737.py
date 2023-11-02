def solution():
    """Patricia has 4 barrels of 7 gallons each. All of them are empty, and there's only one faucet with a flow rate of 3.5 gallons per minute. How many minutes will it take to fill all 4 barrels?"""
    # Define the number of barrels and their volume
    NUM_BARRELS = 4
    BARREL_VOLUME = 7

    # Calculate the total volume to be filled
    total_volume = NUM_BARRELS * BARREL_VOLUME

    # Calculate the time required to fill the barrels
    time_in_minutes = total_volume / 3.5

    # Display the time required in minutes
    result = time_in_minutes
    return result

print(solution())