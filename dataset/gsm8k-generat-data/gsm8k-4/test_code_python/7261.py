def solution():
    """Mr. Fortchaud turns on his heater on the 1st of November, 2005. The fuel tank was then full and contained 3,000 L. On January 1, 2006, the tank counter indicated that 180 L remained. Mr. Fortchaud again filled his tank completely. On 1 May 2006, Mr. Fortchaud decided to stop heating and he read 1,238 L on the meter. What the volume of fuel oil that was used between 1 November 2005 and 1 May 2006?"""
    # Define the initial fuel tank volume and the final fuel tank volume
    initial_volume = 3000
    final_volume = 1238

    # Calculate the volume of fuel used between November 1 and January 1
    used_volume_1 = initial_volume - 180

    # Calculate the volume of fuel used between January 1 and May 1
    used_volume_2 = initial_volume - final_volume

    # Calculate the total volume of fuel used
    total_used_volume = used_volume_1 + used_volume_2

    result = total_used_volume
    return result

print(solution())