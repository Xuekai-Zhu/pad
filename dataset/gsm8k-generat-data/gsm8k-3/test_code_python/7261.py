def solution():
    """Mr. Fortchaud turns on his heater on the 1st of November, 2005. The fuel tank was then full and contained 3,000 L. On January 1, 2006, the tank counter indicated that 180 L remained. Mr. Fortchaud again filled his tank completely. On 1 May 2006, Mr. Fortchaud decided to stop heating and he read 1,238 L on the meter. What the volume of fuel oil that was used between 1 November 2005 and 1 May 2006?"""
    # Define the initial fuel tank volume and the volume remaining on January 1, 2006
    INITIAL_VOLUME = 3000
    JANUARY_REMAINING = 180

    # Calculate the total fuel used between November 1, 2005 and January 1, 2006
    fuel_used_1 = INITIAL_VOLUME - JANUARY_REMAINING

    # Calculate the total fuel used between January 1, 2006 and May 1, 2006
    MAY_REMAINING = 1238
    FILL_VOLUME = INITIAL_VOLUME - MAY_REMAINING
    fuel_used_2 = FILL_VOLUME

    # Calculate the total fuel used between November 1, 2005 and May 1, 2006
    total_fuel_used = fuel_used_1 + fuel_used_2

    # Display the total fuel used
    result = total_fuel_used
    return result

print(solution())