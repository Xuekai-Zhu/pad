def solution():
    instrument_size = 3 #milimeters
    fly_eye_size = 2 #milimeters
    if instrument_size > fly_eye_size:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())