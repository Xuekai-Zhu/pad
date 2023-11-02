def solution():
    """Zach baked cookies for a bake sale. On Monday he baked 32 cookies. On Tuesday he ran out of sugar and could only bake half of the number of cookies he baked the day before. On Wednesday he baked three times the number of cookies he did on Tuesday, but his brother ate 4 of those cookies. How many cookies did he have at the end of the three days?"""
    monday_cookies = 32
    tuesday_cookies = monday_cookies // 2
    wednesday_cookies = 3 * tuesday_cookies - 4
    total_cookies = monday_cookies + tuesday_cookies + wednesday_cookies
    result = total_cookies
    return result

print(solution())