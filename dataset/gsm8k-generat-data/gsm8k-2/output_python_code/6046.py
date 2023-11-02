def solution():
    """Kyle bakes 60 cookies and 32 brownies. Kyle eats 2 cookies and 2 brownies. Kyle's mom eats 1 cookie and 2 brownies.
    If Kyle sells a cookie for $1 and a brownie for $1.50, how much money will Kyle make if he sells all of his baked goods?"""
    cookie_price = 1
    brownie_price = 1.5
    total_cookies = 60
    total_brownies = 32
    cookies_eaten = 2
    brownies_eaten = 2
    cookies_mom_eaten = 1
    brownies_mom_eaten = 2
    cookies_to_sell = total_cookies - cookies_eaten - cookies_mom_eaten
    brownies_to_sell = total_brownies - brownies_eaten - brownies_mom_eaten
    total_money = (cookies_to_sell * cookie_price) + (brownies_to_sell * brownie_price)
    result = total_money
    return result

print(solution())