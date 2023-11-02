def solution():
    """Barbara Blackburn can type 212 words per minute. Due to Carpal tunnel syndrome, Barbara cannot use her left hand for a while so her typing speed is now 40 words less per minute. If she is supposed to type a document with 3440 words, how many minutes will it take her to finish typing the document?"""
    original_speed = 212
    reduced_speed = original_speed - 40
    document_words = 3440
    left_hand_words = document_words / 2
    right_hand_words = document_words / 2
    total_time = (left_hand_words / reduced_speed) + (right_hand_words / original_speed)
    result = total_time
    return result

print(solution())