def solution():
    # Calculate the number of cookies brought by each person
    mona_cookies = 20
    jasmine_cookies = mona_cookies - 5  # Jasmine brought 5 fewer cookies than Mona
    rachel_cookies = jasmine_cookies + 10  # Rachel brought 10 more cookies than Jasmine

    # Calculate the total number of cookies brought by all three people
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies
    result = total_cookies
    return result

print(solution())