def solution():
    weeds_tuesday = 25
    weeds_wednesday = 3 * weeds_tuesday
    weeds_thursday = weeds_wednesday / 5
    weeds_friday = weeds_thursday - 10

    total_weeds = weeds_tuesday + weeds_wednesday + weeds_thursday + weeds_friday
    result = total_weeds
    return result

print(solution())