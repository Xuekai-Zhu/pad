def solution():
    """Betty has a tray of cookies and a tray of brownies. She has a real sweet tooth and eats 3 cookies a day and 1 brownie a day. If she starts with 60 cookies and 10 brownies, how many more cookies than brownies does she have after a week of eating like this?"""
    # Define the number of cookies and brownies Betty starts with
    cookies = 60
    brownies = 10

    # Calculate the number of cookies and brownies Betty will have after a week
    cookies_left = cookies - (3 * 7)
    brownies_left = brownies - (1 * 7)

    # Calculate the difference between the number of cookies and brownies left
    difference = cookies_left - brownies_left

    result = difference
    return result

print(solution())