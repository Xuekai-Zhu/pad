def solution():
    """Kyle bakes 60 cookies and 32 brownies. Kyle eats 2 cookies and 2 brownies. Kyle's mom eats 1 cookie and 2 brownies. If Kyle sells a cookie for $1 and a brownie for $1.50, how much money will Kyle make if he sells all of his baked goods?"""
    # Define the number of cookies and brownies baked
    cookies_baked = 60
    brownies_baked = 32

    # Define the amount of cookies and brownies eaten by Kyle and his mom
    cookies_eaten = 2 + 1
    brownies_eaten = 2 + 2

    # Calculate the total number of cookies and brownies available for sale
    cookies_available = cookies_baked - cookies_eaten
    brownies_available = brownies_baked - brownies_eaten

    # Calculate the total amount of money Kyle can make by selling his baked goods
    cookies_sales = cookies_available * 1
    brownies_sales = brownies_available * 1.5
    total_sales = cookies_sales + brownies_sales

    result = total_sales
    return result

print(solution())