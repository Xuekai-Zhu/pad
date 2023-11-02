def solution():
    # Calculate the total amount of flour
    total_flour = 4 * 5

    # Calculate the number of batches Matt can make
    num_batches = total_flour // 2

    # Calculate the total number of cookies
    total_cookies = num_batches * 12

    # Calculate the number of cookies left after Jim eats 15
    cookies_left = total_cookies - 15

    result = cookies_left
    return result

print(solution())