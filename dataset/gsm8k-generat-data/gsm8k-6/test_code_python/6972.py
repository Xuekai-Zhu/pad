def solution():
    # Calculate the total number of cookies in the box
    total_cookies = 20 * 4 * 4  # 4 bags with 20 cookies each

    # Calculate the total number of calories in the box
    total_calories = total_cookies * 20  # each cookie has 20 calories

    result = total_calories
    return result

print(solution())