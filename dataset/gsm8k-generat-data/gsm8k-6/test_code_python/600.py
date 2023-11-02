def solution():
    original_speed = 65
    reduced_speed = original_speed - 20
    document_length = 810
    time_with_original_speed = document_length / original_speed
    time_with_reduced_speed = document_length / reduced_speed
    time_difference = time_with_original_speed - time_with_reduced_speed
    result = time_difference * 60  # converting hours to minutes
    return result

print(solution())