def solution():
     oreos = 4
     cookies = 9
     price_oreo = 2
     price_cookie = 3
     total_items = 65
     total_oreos = total_items * (oreos / (oreos + cookies))
     total_cookies = total_items * (cookies / (oreos + cookies))
     cost_oreos = total_oreos * price_oreo
     cost_cookies = total_cookies * price_cookie
     difference = cost_cookies - cost_oreos
     result = difference
     return result

print(solution())