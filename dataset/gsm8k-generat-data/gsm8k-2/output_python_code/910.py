def solution():
    """It took an alligator named Paul 4 hours to walk from his home at the River Nile to the Nile Delta. On the return journey, Paul traveled with six other alligators, the journey taking 2 more hours than Paul took to walk to the Nile Delta, to reach their home at the River Nile. What's the combined time the alligators walked?"""
    paul_time = 4
    combined_time = paul_time + 2 + (paul_time * 6)
    result = combined_time
    return result

print(solution())