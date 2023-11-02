def solution():
    # Define the initial number of white cookies and the difference in number between black and white cookies
    white_cookies = 80
    black_white_diff = 50
    
    # Calculate the initial number of black cookies
    black_cookies = white_cookies + black_white_diff
    
    # Calculate the number of black cookies remaining after Cristian eats half of them
    black_cookies_remaining = 0.5 * black_cookies
    
    # Calculate the number of white cookies remaining after Cristian eats 3/4 of them
    white_cookies_remaining = 0.25 * white_cookies
    
    # Calculate the total number of cookies remaining
    total_cookies_remaining = black_cookies_remaining + white_cookies_remaining
    
    result = total_cookies_remaining
    return result

print(solution())