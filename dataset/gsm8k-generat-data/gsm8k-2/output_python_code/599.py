def solution():
    """Mike can type 65 words per minute. Due to a minor accident, Mike cannot use his right hand for a while so that his typing speed is now 20 words less per minute. If he is supposed to type a document with 810 words, how many minutes will it take him to finish typing the document?"""
    original_typing_speed = 65
    reduced_typing_speed = original_typing_speed - 20
    document_length = 810
    time_with_original_speed = document_length / original_typing_speed
    time_with_reduced_speed = document_length / reduced_typing_speed
    result = time_with_original_speed + time_with_reduced_speed
    return result

print(solution())