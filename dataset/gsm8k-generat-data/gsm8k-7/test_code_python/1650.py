def solution():
    num_neighbors = 15
    cookies_per_neighbor = 10
    total_cookies = num_neighbors * cookies_per_neighbor
    cookies_left = 8
    cookies_taken = total_cookies - cookies_left
    cookies_per_correct_neighbor = cookies_per_neighbor
    cookies_taken_by_correct_neighbors = cookies_per_correct_neighbor * (num_neighbors - 1)
    cookies_taken_by_sarah = cookies_taken - cookies_taken_by_correct_neighbors
    result = cookies_taken_by_sarah
    return result

print(solution())