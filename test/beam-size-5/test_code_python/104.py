def solution():
    # Calculate the number of cookies Henry wants to make last year
    cookies_last_year = 2 * 110  # Henry wants to make twice as many cookies as he did last year
    cookies_made = cookies_last_year + 15  # Henry actually baked 15 more cookies than he meant to

    # Calculate the number of cookies Henry drops out to cool
    cookies_dropped = 5

    # Calculate the number of cookies Henry baked last year
    cookies_last_year = cookies_made - cookies_dropped - cookies_last_year
    result = cookies_last_year
    return result

print(solution())