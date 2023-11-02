def solution():
    current_phrases = 17
    starting_phrases = 3
    phrases_per_week = 2

    # Calculate the number of weeks it has taken to teach the parrot current phrases
    num_weeks = (current_phrases - starting_phrases) / phrases_per_week

    # Calculate the number of days Georgina has had the parrot
    num_days = num_weeks * 7
    result = num_days
    return result

print(solution())