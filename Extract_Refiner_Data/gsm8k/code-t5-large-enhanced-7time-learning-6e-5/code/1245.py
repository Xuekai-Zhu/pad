def solution():
    
    # Define the number of rooms and people in the house
    num_rooms = 8
    num_people = 4

    # Calculate the number of flashlights
    num_flashlights = num_rooms * 2

    # Calculate the number of small and medium candles
    num_small_candles = num_rooms / 2
    num_medium_candles = num_rooms / 2

    # Calculate the total number of candles
    total_candles = (num_small_candles * 4) + (num_medium_candles * 5)

    # Calculate the total number of candles and flashlights
    total_candles_and_flashlights = num_flashlights + total_candles

    # Display the total number of candles and flashlights
    result = total_candles_and_flashlights
    return result

print(solution())