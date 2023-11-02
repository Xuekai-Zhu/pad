def solution():
    """Kyle bakes 60 cookies and 32 brownies. Kyle eats 2 cookies and 2 brownies. Kyle's mom eats 1 cookie and 2 brownies. If Kyle sells a cookie for $1 and a brownie for $1.50, how much money will Kyle make if he sells all of his baked goods?"""
    cookies_baked = 60
    brownies_baked = 32
    cookies_eaten = 2
    brownies_eaten = 2
    cookies_mom_eats = 1
    brownies_mom_eats = 2
    cookies_left = cookies_baked - cookies_eaten - cookies_mom_eats
    brownies_left = brownies_baked - brownies_eaten - brownies_mom_eats
    cookie_price = 1
    brownie_price = 1.5
    money_made = cookies_left * cookie_price + brownies_left * brownie_price
    result = money_made
    return result

print(solution())