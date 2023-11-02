def solution():
    # Convert 3 dozen cookies to regular count
    morning_cookies = 3 * 12

    # Calculate total cookies sold
    total_sold = morning_cookies + 57 + 16

    # Calculate cookies left to take home
    cookies_left = 120 - total_sold
    result = cookies_left
    return result

print(solution())