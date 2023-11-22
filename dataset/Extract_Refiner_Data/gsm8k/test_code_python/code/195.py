def solution():
    
    # Define the number of sentences each publisher receives
    PUBLISHER_SENTENCES = 2

    # Define the rate of paying each person per sentence
    PRICE_PER_SENTENCE = 0.05

    # Calculate the total number of sentences each publisher receives
    total_publishers = PUBLISHER_SENTENCES * 2

    # Calculate the number of sentences each person receives
    sentence_A = 1000 - (total_publishers * PRICE_PER_SENTENCE)
    sentence_B = 2 * sentence_A

    # Calculate Mark's earnings per week
    earnings_per_week = (sentence_A + sentence_B) * 100

    # Display Mark's earnings per week
    result = earnings_per_week
    return result

print(solution())