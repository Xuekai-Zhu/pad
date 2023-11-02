def solution():
    """Mona brought 20 cookies to share in class. Jasmine brought 5 fewer cookies than Mona. Rachel brought 10 more cookies than Jasmine. How many cookies altogether did Mona, Jasmine, and Rachel bring to share in class?"""
    mona_cookies = 20
    jasmine_cookies = mona_cookies - 5
    rachel_cookies = jasmine_cookies + 10
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies
    result = total_cookies
    return result

print(solution())