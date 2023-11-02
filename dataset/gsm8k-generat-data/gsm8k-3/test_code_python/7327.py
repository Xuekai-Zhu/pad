def solution():
    """Betty has a tray of cookies and a tray of brownies.  She has a real sweet tooth and eats 3 cookies a day and 1 brownie a day.  If she starts with 60 cookies and 10 brownies, how many more cookies than brownies does she have after a week of eating like this?"""
    # Define the number of cookies and brownies Betty starts with
    initial_cookies = 60
    initial_brownies = 10

    # Calculate how many cookies and brownies Betty eats in a week
    cookies_eaten = 3 * 7
    brownies_eaten = 1 * 7

    # Calculate how many cookies and brownies Betty has left after the week
    cookies_left = initial_cookies - cookies_eaten
    brownies_left = initial_brownies - brownies_eaten

    # Calculate how many more cookies than brownies Betty has left
    difference = cookies_left - brownies_left

    # Display the difference
    result = difference
    return result

print(solution())