def solution():
    jessy_jokes = 11
    alan_jokes = 7

    # Calculate the total number of jokes they told this past Saturday
    total_jokes = jessy_jokes + alan_jokes

    # Double the number of jokes for next Saturday
    doubled_jokes = total_jokes * 2

    # Calculate the total number of jokes they will have told after next Saturday
    total_jokes_so_far = doubled_jokes + total_jokes
    result = total_jokes_so_far
    return result

print(solution())