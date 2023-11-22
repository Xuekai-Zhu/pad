def solution():
    
    # Define the tap rates and the total time raised
    RATE_RIGHT_FOOT = 300
    RATE_LEFT_FOOT = 250
    TAPS_PER_MINUTE = 200
    TOTAL_TIME = 5

    # Calculate the number of taps Helga taps right foot
    taps_right_foot = RATE_RIGHT_FOOT * TAPS_PER_MINUTE

    # Calculate the number of taps Helga taps left foot
    taps_left_foot = RATE_LEFT_FOOT * TAPS_PER_MINUTE

    # Calculate the number of taps Helga taps arms during the dance
    taps_arms = TAPS_PER_MINUTE * TOTAL_TIME

    # Calculate the combined total number of times Helga taps both of her feet
    total_taps = taps_right_foot + taps_left_foot + taps_arms

    # Display the combined total number of times Helga taps both of her feet
    result = total_t

print(solution())