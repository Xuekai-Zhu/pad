def solution():
    
    # Define the time it takes to row one feet of water
    TIME_PER_FEET = 15 / 10

    # Define the time it takes to row the twenty feet of water
    TIME_TO_ROW_TWENTY_FEET = 20

    # Define the total time to row the boat
    total_time = 64

    # Calculate the time it takes to row the water
    time_to_row = TIME_TO_ROW_TWENTY_FEET * TIME_TO_ROW_TWENTY_FEET

    # Calculate the amount of water taken on by the boat
    water_taken_on = total_time - time_to_row

    # Display the amount of water taken on
    result = water_taken_on
    return result

print(solution())