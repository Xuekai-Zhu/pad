def solution():
    """Mike can type 65 words per minute. Due to a minor accident, 
    Mike cannot use his right hand for a while so that his typing speed 
    is now 20 words less per minute. If he is supposed to type a document 
    with 810 words, how many minutes will it take him to finish typing the document?"""
    original_speed = 65
    reduced_speed = original_speed - 20
    words_to_type = 810
    time_at_original_speed = words_to_type / original_speed
    time_at_reduced_speed = words_to_type / reduced_speed
    extra_time = time_at_reduced_speed - time_at_original_speed
    result = time_at_reduced_speed
    
    return result

print(solution())