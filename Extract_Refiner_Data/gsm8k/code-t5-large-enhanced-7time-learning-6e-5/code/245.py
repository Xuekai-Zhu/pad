def solution():
    
    # Define the number of cookies eaten on each day
    monday_cookies = 5
    tuesday_cookies = monday_cookies * 2

    # Calculate the total number of cookies eaten
    total_cookies = monday_cookies + tuesday_cookies

    # Calculate the number of calories consumed by Sue
    sue_calories = sue_cookies * 200

    # Calculate the difference in calories consumed
    calorie_difference = sue_calories - monday_cookies

    # return the result
    result = calorie_difference
    return result

print(solution())