def solution():
    known_phrases = 17  # The parrot knows 17 phrases
    phrases_taught_per_week = 2  # Georgina teaches the parrot 2 phrases per week
    phrases_known_when_bought = 3  # The parrot already knew 3 phrases when Georgina bought it

    # Calculate the total number of phrases taught
    total_phrases_taught = known_phrases - phrases_known_when_bought

    # Calculate the number of weeks it took to teach the parrot all of the known phrases
    weeks_to_teach_all_phrases = total_phrases_taught / phrases_taught_per_week

    # Convert weeks to days
    days_owned = weeks_to_teach_all_phrases * 7
    result = days_owned
    return result

print(solution())