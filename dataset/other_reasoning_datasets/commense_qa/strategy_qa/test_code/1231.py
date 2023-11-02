def solution():
    snowdown_precipitation_inches = 200
    bowling_pin_height_inches = 15
    if snowdown_precipitation_inches > bowling_pin_height_inches:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())