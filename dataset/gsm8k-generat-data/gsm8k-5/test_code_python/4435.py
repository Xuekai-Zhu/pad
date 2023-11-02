def solution():
    milk_cost = 3
    cereal_cost = 3.5
    banana_cost = 0.25
    apple_cost = 0.5
    
    # Calculate the total cost of milk, cereal, bananas and apples
    total_cost = milk_cost + (2 * cereal_cost) + (4 * banana_cost) + (4 * apple_cost)
    
    # Calculate the remaining amount that Steve spent on cookies
    cookies_cost = 25 - total_cost - (2 * milk_cost)
    
    # Calculate the cost per box of cookies
    cookie_cost_per_box = milk_cost * 2
    
    # Calculate the number of boxes of cookies Steve bought
    num_cookies_boxes = cookies_cost / cookie_cost_per_box
    
    result = num_cookies_boxes
    return result

print(solution())