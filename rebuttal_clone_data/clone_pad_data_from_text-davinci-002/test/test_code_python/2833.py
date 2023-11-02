def solution():
    cookies_in_a_bag = 7
    cookies_in_a_box = 12
    cookies_in_8_boxes = 8 * cookies_in_a_box
    cookies_in_9_bags = 9 * cookies_in_a_bag
    difference = cookies_in_8_boxes - cookies_in_9_bags
    result = difference
    return result

print(solution())