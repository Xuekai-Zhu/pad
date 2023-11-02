def solution():
    """Edna made cookies for all of her neighbors and left the cookies outside for them to take. She made 150 cookies so her 15 neighbors could get 10 cookies each. However, the neighbor who arrived last told Edna there were only 8 cookies left. Edna thinks it was Sarah who took too many cookies. If all the other neighbors took the correct amount of cookies, how many cookies did Sarah take?"""
    # Define the total number of cookies and number of neighbors
    TOTAL_COOKIES = 150
    NUM_NEIGHBORS = 15

    # Calculate the expected number of cookies per neighbor
    expected_cookies = TOTAL_COOKIES // NUM_NEIGHBORS

    # Calculate the total number of cookies taken by all neighbors except Sarah
    total_taken = (NUM_NEIGHBORS - 1) * expected_cookies

    # Calculate the number of cookies taken by Sarah
    cookies_sarah = TOTAL_COOKIES - total_taken - 8

    # Display the number of cookies taken by Sarah
    result = cookies_sarah
    return result

print(solution())