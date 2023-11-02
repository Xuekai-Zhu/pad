def solution():
    """Kyle bakes 60 cookies and 32 brownies. Kyle eats 2 cookies and 2 brownies.
    Kyle's mom eats 1 cookie and 2 brownies. If Kyle sells a cookie for $1 and a brownie for $1.50,
    how much money will Kyle make if he sells all of his baked goods?"""
    # Define the number of cookies and brownies baked
    num_cookies = 60
    num_brownies = 32

    # Define the number of cookies and brownies eaten by Kyle and his mom
    num_cookies_eaten = 2 + 1
    num_brownies_eaten = 2 + 2

    # Determine the number of cookies and brownies remaining to sell
    num_cookies_remaining = num_cookies - num_cookies_eaten
    num_brownies_remaining = num_brownies - num_brownies_eaten

    # Determine the total revenue from selling the remaining cookies and brownies
    revenue_from_cookies = num_cookies_remaining * 1
    revenue_from_brownies = num_brownies_remaining * 1.5
    total_revenue = revenue_from_cookies + revenue_from_brownies

    # Display the total revenue
    result = total_revenue
    return result

print(solution())