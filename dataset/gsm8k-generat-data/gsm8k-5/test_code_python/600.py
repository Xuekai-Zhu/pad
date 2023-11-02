def solution():
    original_speed = 65  # Mike's original typing speed is 65 words per minute
    reduced_speed = original_speed - 20  # After the accident, Mike's typing speed is reduced by 20 words per minute
    document_length = 810  # Mike needs to type a document with 810 words

    # Calculate the time it would take Mike to type the document with his original speed
    time_with_original_speed = document_length / original_speed

    # Calculate the time it would take Mike to type the document with his reduced speed
    time_with_reduced_speed = document_length / reduced_speed

    # The time it would take Mike to type the document is the maximum of the two times calculated above
    time_to_type_document = max(time_with_original_speed, time_with_reduced_speed)
    result = time_to_type_document
    return result

print(solution())