def solution():
    """Mr. Fortchaud turns on his heater on the 1st of November, 2005. The fuel tank was then full and contained
    3,000 L. On January 1, 2006, the tank counter indicated that 180 L remained. Mr. Fortchaud again filled his tank
    completely. On 1 May 2006, Mr. Fortchaud decided to stop heating and he read 1,238 L on the meter. What the volume
    of fuel oil that was used between 1 November 2005 and 1 May 2006?"""
    initial_volume = 3000
    final_volume = 1238
    volume_before_refill = 180
    total_volume_used = initial_volume - volume_before_refill + final_volume
    result = total_volume_used
    return result

print(solution())