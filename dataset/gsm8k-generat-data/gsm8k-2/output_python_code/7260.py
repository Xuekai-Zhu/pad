def solution():
    """Mr. Fortchaud turns on his heater on the 1st of November, 2005. The fuel tank was then full and contained 3,000 L. On January 1, 2006, the tank counter indicated that 180 L remained. Mr. Fortchaud again filled his tank completely. On 1 May 2006, Mr. Fortchaud decided to stop heating and he read 1,238 L on the meter. What the volume of fuel oil that was used between 1 November 2005 and 1 May 2006?"""
    starting_volume = 3000
    first_refill = starting_volume - 180
    second_refill = 3000 - first_refill
    ending_volume = 1238
    used_volume = starting_volume - second_refill - ending_volume
    result = used_volume
    return result

print(solution())