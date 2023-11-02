def solution():
    total_cookies = 150
    num_neighbors = 15
    cookies_per_neighbor = 10
    cookies_left = 8
    cookies_taken_correctly = (num_neighbors * cookies_per_neighbor) - cookies_left
    cookies_taken_by_sarah = total_cookies - cookies_taken_correctly
    result = cookies_taken_by_sarah
    return result

print(solution())