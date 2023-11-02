def solution():
    """Zach baked cookies for a bake sale. On Monday he baked 32 cookies. On Tuesday he ran out of sugar and could only bake half of the number of cookies he baked the day before. On Wednesday he baked three times the number of cookies he did on Tuesday, but his brother ate 4 of those cookies. How many cookies did he have at the end of the three days?"""
    # Calculate the number of cookies baked on Tuesday
    cookies_tuesday = 32 // 2

    # Calculate the number of cookies baked on Wednesday
    cookies_wednesday = cookies_tuesday * 3 - 4

    # Calculate the total number of cookies
    total_cookies = 32 + cookies_tuesday + cookies_wednesday

    # Display the total number of cookies
    result = total_cookies
    return result

print(solution())