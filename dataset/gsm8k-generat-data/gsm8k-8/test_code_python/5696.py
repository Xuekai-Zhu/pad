def solution():
    # Define the number of known phrases and the number of phrases learned per week
    known_phrases = 17
    phrases_per_week = 2

    # Define the number of phrases known when the parrot was bought
    initial_known_phrases = 3

    # Calculate the number of weeks it took to teach the parrot all its current phrases
    weeks_to_teach = (known_phrases - initial_known_phrases) / phrases_per_week

    # Calculate the number of days Georgina has had the parrot
    days_owned = weeks_to_teach * 7
    result = days_owned
    return result

print(solution())