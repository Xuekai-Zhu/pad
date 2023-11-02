def solution():
    """Edna made cookies for all of her neighbors and left the cookies outside for them to take. She made 150 cookies so her 15 neighbors could get 10 cookies each. However, the neighbor who arrived last told Edna there were only 8 cookies left. Edna thinks it was Sarah who took too many cookies. If all the other neighbors took the correct amount of cookies, how many cookies did Sarah take?"""
    # Define the total number of cookies and neighbors
    total_cookies = 150
    total_neighbors = 15

    # Calculate the number of cookies each neighbor should take
    correct_cookies_per_neighbor = total_cookies // total_neighbors

    # Calculate the number of cookies taken by all neighbors except Sarah
    cookies_taken_except_sarah = (total_neighbors - 1) * correct_cookies_per_neighbor

    # Calculate the number of cookies taken by Sarah
    cookies_taken_by_sarah = total_cookies - cookies_taken_except_sarah - 8

    # Return the result
    result = cookies_taken_by_sarah
    return result

print(solution())