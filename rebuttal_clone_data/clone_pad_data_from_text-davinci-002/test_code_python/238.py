def solution():
     """Jack is running a bake sale to help pay for his basketball team's uniforms. He's already sold 4 brownies for $3 each and 5 lemon squares for $2 each. If Jack's goal is to make $50 and he sells cookies for $4 each, how many cookies does he need to sell to reach his goal?"""
     brownies_sold = 4
     lemon_squares_sold = 5
     cookies_sold = 0
     price_per_brownie = 3
     price_per_lemon_square = 2
     price_per_cookie = 4
     total_money_made = (brownies_sold * price_per_brownie) + (lemon_squares_sold * price_per_lemon_square)
     goal = 50
     while total_money_made < goal:
         cookies_sold += 1
         total_money_made = (brownies_sold * price_per_brownie) + (lemon_squares_sold * price_per_lemon_square) + (cookies_sold * price_per_cookie)
     result = cookies_sold

print(solution())