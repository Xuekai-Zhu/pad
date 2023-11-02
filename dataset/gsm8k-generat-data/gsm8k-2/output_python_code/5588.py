def solution():
    """Michael saved 5 of his cookies to give Sarah, who saved a third of her 9 cupcakes to give to Michael. How many desserts does Sarah end up with?"""
    michael_cookies = 5
    sarah_cupcakes = 9 / 3
    sarah_desserts = sarah_cupcakes + michael_cookies
    result = sarah_desserts
    return result

print(solution())