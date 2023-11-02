def solution():
    event_year = 2017
    current_year = 2021
    years_since_event = current_year - event_year
    if years_since_event <= 5:
        result = "yes"
    else:
        result = "no"
    return result

# Explanation: The relevance of Ariana Grande as a topic in a PTSD presentation diminishes as time goes on, hence the comparison to five years.

print(solution())