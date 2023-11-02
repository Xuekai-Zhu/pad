def solution():
    # Calculate the total number of cookies Annie ate in 3 days
    monday = 5
    tuesday = 2 * monday
    wednesday = tuesday * 1.4  # 40% more than tuesday
    total_cookies = monday + tuesday + wednesday
    result = total_cookies
    return result

print(solution())