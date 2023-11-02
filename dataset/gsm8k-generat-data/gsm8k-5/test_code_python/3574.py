def solution():
    total_cookies = 60
    nuts_percentage = 0.25
    chocolate_percentage = 0.4

    # Calculate the number of cookies that will have nuts and chocolate chips
    nuts_and_chocolate_cookies = total_cookies * (1 - nuts_percentage - chocolate_percentage)

    # Calculate the total number of nuts Maria needs to add to the cookies
    nuts_needed = (total_cookies * nuts_percentage * 2) + (nuts_and_chocolate_cookies * 2)
    result = nuts_needed
    return result

print(solution())