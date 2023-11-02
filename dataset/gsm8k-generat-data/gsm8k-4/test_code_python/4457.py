def solution():
    """Matt can make a batch of a dozen cookies using 2 pounds of flour. He uses 4 bags of flour each weighing 5 pounds. If Jim eats 15 cookies how many cookies are left?"""
    # Define the amount of flour used to make 1 dozen cookies
    flour_per_dozen = 2

    # Calculate the total amount of flour used
    total_flour = 4 * 5

    # Calculate the total number of cookies
    total_cookies = (total_flour / flour_per_dozen) * 12

    # Calculate the number of cookies left after Jim eats 15
    cookies_left = total_cookies - 15

    result = cookies_left
    return result

print(solution())