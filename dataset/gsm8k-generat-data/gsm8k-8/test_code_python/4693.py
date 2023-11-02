def solution():
    original_speed = 212
    reduced_speed = 172
    document_length = 3440

    # Calculate how long it would take Barbara to type the whole document at her original speed
    time_at_original_speed = document_length / original_speed

    # Calculate how many words she can still type with only one hand
    words_with_one_hand = time_at_original_speed * reduced_speed

    # Calculate how long it would take her to type the remaining words with one hand
    remaining_words = document_length - words_with_one_hand
    time_with_one_hand = remaining_words / reduced_speed

    # Add the times together to get the total time
    total_time = time_at_original_speed + time_with_one_hand
    result = total_time
    return result

print(solution())