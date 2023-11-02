def solution():
    # Define the volume of one bucket of water
    bucket_volume = 120

    # Calculate the total volume of water used to fill the bathtub
    total_volume = bucket_volume * 14

    # Calculate the volume of water used for one bath
    bath_volume = total_volume / 14 - bucket_volume * 3

    # Calculate the volume of water used for one week of baths
    weekly_volume = bath_volume * 7
    result = weekly_volume
    return result

print(solution())