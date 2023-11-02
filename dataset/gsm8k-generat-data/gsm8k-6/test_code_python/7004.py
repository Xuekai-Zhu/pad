def solution():
    # Calculate the total number of jokes Jessy and Alan told this past Saturday
    total_jokes = 11 + 7

    # Calculate the total number of jokes they would have told next Saturday
    next_saturday_jokes = 2 * total_jokes

    # Calculate the total number of jokes they would have told together so far
    total_jokes_so_far = total_jokes + next_saturday_jokes
    result = total_jokes_so_far
    return result

print(solution())