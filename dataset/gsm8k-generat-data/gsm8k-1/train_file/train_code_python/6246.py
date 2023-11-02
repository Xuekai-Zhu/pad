def solution():
    """Graeme is weighing cookies to see how many he can fit in his box. His box can only hold 40 pounds of cookies. If each cookie weighs 2 ounces, how many cookies can he fit in the box?"""
    box_capacity = 40 * 16  # convert pounds to ounces
    cookie_weight = 2
    cookies_per_box = box_capacity // cookie_weight
    result = cookies_per_box
    return result

print(solution())