def solution():
     """Dan owns an ice cream shop and every sixth customer gets a free ice cream cone. Cones cost $2 each. If he sold $100 worth of cones, how many free ones did he give away?"""
     cone_price = 2
     total_cone_sales = 100
     total_cones_given_away = total_cone_sales / 6
     result = total_cones_given_away
     return result

print(solution())