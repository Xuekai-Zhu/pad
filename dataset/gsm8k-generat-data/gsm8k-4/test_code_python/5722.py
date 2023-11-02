def solution():
    """Mona brought 20 cookies to share in class. Jasmine brought 5 fewer cookies than Mona. Rachel brought 10 more cookies than Jasmine. How many cookies altogether did Mona, Jasmine, and Rachel bring to share in class?"""
    # Define the number of cookies Mona brought
    mona_cookies = 20

    # Calculate the number of cookies Jasmine brought
    jasmine_cookies = mona_cookies - 5

    # Calculate the number of cookies Rachel brought
    rachel_cookies = jasmine_cookies + 10

    # Calculate the total number of cookies brought
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies

    # return the result
    result = total_cookies
    return result

print(solution())