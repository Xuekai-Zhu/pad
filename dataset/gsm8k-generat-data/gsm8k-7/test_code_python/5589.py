def solution():
    michael_cookies = 5
    sarah_cupcakes = 9 / 3

    # Sarah gives away a third of her cupcakes, so she keeps 2/3 of them
    sarah_remaining_cupcakes = sarah_cupcakes * (2/3)

    # Sarah receives 5 cookies from Michael
    sarah_total_desserts = sarah_remaining_cupcakes + michael_cookies
    result = sarah_total_desserts
    return result

print(solution())