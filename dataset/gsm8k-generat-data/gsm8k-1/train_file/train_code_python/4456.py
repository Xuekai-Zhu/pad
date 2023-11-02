def solution():
    """Matt can make a batch of a dozen cookies using 2 pounds of flour. He uses 4 bags of flour each weighing 5 pounds. If Jim eats 15 cookies how many cookies are left?"""
    cookies_per_dozen = 12
    flour_per_dozen = 2
    bags_of_flour = 4
    weight_of_flour_per_bag = 5
    total_flour = bags_of_flour * weight_of_flour_per_bag
    total_cookies = (cookies_per_dozen / flour_per_dozen) * total_flour
    cookies_left = total_cookies - 15
    result = cookies_left
    return result

print(solution())