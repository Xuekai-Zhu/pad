def solution():
     day_length = 24
     sleep_fraction = 1/3
     school_fraction = 1/6
     assignment_fraction = 1/12
     family_fraction = 1 - (sleep_fraction + school_fraction + assignment_fraction)
     family_time = day_length * family_fraction
     result = family_time
     
     return result

print(solution())