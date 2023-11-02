def solution():
    typing_speed = 6  # Janice types 6 sentences per minute
    total_typing_time = 20 + 15 + 18  # Janice typed for a total of 20 + 15 + 18 = 53 minutes
    total_sentences_typed = (total_typing_time * typing_speed) - 40  # Janice typed for a total of 53 minutes, but deleted 40 incorrect sentences
    initial_sentences = 536 - total_sentences_typed  # Janice started with a total of 536 sentences, but typed a certain number and deleted 40
    result = initial_sentences
    return result

print(solution())