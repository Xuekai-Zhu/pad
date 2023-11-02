def solution():
    """Edna made cookies for all of her neighbors and left the cookies outside for them to take. She made 150 cookies so her 15 neighbors could get 10 cookies each. However, the neighbor who arrived last told Edna there were only 8 cookies left. Edna thinks it was Sarah who took too many cookies. If all the other neighbors took the correct amount of cookies, how many cookies did Sarah take?"""
    total_cookies = 150
    num_neighbors = 15
    correct_cookies_per_neighbor = 10
    cookies_left = 8
    cookies_taken_by_others = (num_neighbors - 1) * correct_cookies_per_neighbor
    cookies_taken_by_sarah = total_cookies - cookies_taken_by_others - cookies_left
    result = cookies_taken_by_sarah
    return result

print(solution())