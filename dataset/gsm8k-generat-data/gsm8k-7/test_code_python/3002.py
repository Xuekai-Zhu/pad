def solution():
    num_trays = 3
    cookies_per_tray = 80
    cookies_per_box = 60
    cost_per_box = 3.5

    # Calculate the total number of cookies needed
    total_cookies = num_trays * cookies_per_tray

    # Calculate the total number of boxes needed
    total_boxes = total_cookies // cookies_per_box + 1

    # Calculate the total cost of all boxes needed
    total_cost = total_boxes * cost_per_box
    result = total_cost
    return result

print(solution())