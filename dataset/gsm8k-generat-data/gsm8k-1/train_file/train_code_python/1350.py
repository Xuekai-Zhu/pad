def solution():
    """Jake sold 10 more stuffed animals than Thor. Quincy sold ten times as many stuffed animals as Thor. If Quincy sold 200 stuffed animals, how many more stuffed animals did Quincy sell than Jake?"""
    quincy_sales = 200
    thor_sales = quincy_sales / 10
    jake_sales = thor_sales - 10
    diff = quincy_sales - jake_sales
    result = diff
    return result

print(solution())