def solution():
    # Calculate the total number of cookies and brownies after Kyle and his mom eats some
    total_cookies = 60 - 2 - 1
    total_brownies = 32 - 2 - 2

    # Calculate the total money made by selling all the baked goods
    total_money = total_cookies * 1 + total_brownies * 1.5
    result = total_money
    return result

print(solution())