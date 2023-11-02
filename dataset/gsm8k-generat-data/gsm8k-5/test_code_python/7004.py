def solution():
    # Calculate the total number of jokes in the past Saturday
    past_saturday_jokes = 11 + 7  # Jessy told 11 jokes, and Alan told 7

    # Calculate the number of jokes they would tell next Saturday if they doubled the number of jokes they told
    next_saturday_jokes = 2 * past_saturday_jokes

    # Calculate the total number of jokes they would have told so far
    total_jokes = past_saturday_jokes + next_saturday_jokes
    result = total_jokes
    return result

print(solution())