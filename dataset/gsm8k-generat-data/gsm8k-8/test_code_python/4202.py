def solution():
    # Calculate the total time it takes to make and decorate one cookie
    total_time_per_cookie = 15 + 30 + 30 + 60  # 15 minutes to bake, 30 to cool, 30 to white ice, 30 to chocolate ice

    # Calculate the number of cookies Elsa can make in 2 hours
    total_cookies = (2*60) // total_time_per_cookie

    # Calculate the total time it takes to make the dough and cool the cookies before dipping
    dough_and_cooling_time = total_cookies * 15

    result = dough_and_cooling_time
    return result

print(solution())