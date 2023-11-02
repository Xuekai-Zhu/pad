def solution():
    # Define the number of cookies Mona brought
    mona_cookies = 20
    
    # Calculate the number of cookies Jasmine brought
    jasmine_cookies = mona_cookies - 5
    
    # Calculate the number of cookies Rachel brought
    rachel_cookies = jasmine_cookies + 10
    
    # Calculate the total number of cookies
    total_cookies = mona_cookies + jasmine_cookies + rachel_cookies
    
    result = total_cookies
    return result

print(solution())