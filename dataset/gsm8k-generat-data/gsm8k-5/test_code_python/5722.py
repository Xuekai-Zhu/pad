def solution():
    mona_cookies = 20  # Mona brought 20 cookies
    jasmine_cookies = mona_cookies - 5  # Jasmine brought 5 fewer cookies than Mona
    rachel_cookies = jasmine_cookies + 10  # Rachel brought 10 more cookies than Jasmine

    # Calculate the total number of cookies brought by all three
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies
    result = total_cookies
    return result

print(solution())