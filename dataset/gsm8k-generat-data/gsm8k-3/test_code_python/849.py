def solution():
    """A hot air balloon with 200 balloons is blowing up. After about half an hour, 1/5 of the total number of balloons in the hot air balloon have blown up. After another hour, twice the number of balloons that had already blown up also blow up. How many balloons in the hot air balloon remain intact?"""
    # Define the initial number of balloons
    INITIAL_BALLOONS = 200

    # Calculate the number of balloons blown up after half an hour
    half_hour_balloons = INITIAL_BALLOONS // 5

    # Calculate the remaining number of balloons
    remaining_balloons = INITIAL_BALLOONS - half_hour_balloons

    # Calculate the number of balloons blown up after another hour
    hour_balloons = 2 * half_hour_balloons

    # Calculate the final remaining number of balloons
    final_balloons = remaining_balloons - hour_balloons

    # Display the final remaining number of balloons
    result = final_balloons
    return result

print(solution())