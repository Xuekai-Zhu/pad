def solution():
    
    total_students = 600
    marching_band_students = total_students / 5
    brass_instrument_students = marching_band_students / 2
    saxophone_students = brass_instrument_students / 5
    alto_saxophone_students = saxophone_students / 3
    result = alto_saxophone_students
    return result

print(solution())