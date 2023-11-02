def solution():
    
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