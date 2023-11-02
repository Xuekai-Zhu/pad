def solution():
    sentences_per_minute = 6
    initial_typing_time = 20
    additional_typing_time = 15
    erasures = 40
    additional_typing_time2 = 18
    total_sentences = 536

    # Calculate the total number of sentences Janice typed before erasing
    initial_sentences = (sentences_per_minute * initial_typing_time) + (sentences_per_minute * additional_typing_time)

    # Calculate the net number of sentences Janice typed after erasing
    net_sentences = total_sentences - erasures

    # Calculate the total number of sentences Janice started with today
    total_initial_sentences = net_sentences - (sentences_per_minute * additional_typing_time2) - initial_sentences
    result = total_initial_sentences
    return result

print(solution())