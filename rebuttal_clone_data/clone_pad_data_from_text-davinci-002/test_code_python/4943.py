def solution():
     half_gallons_needed = 10
     cookies_baked = 40
     cookies_needed = 200 * 12
     result = half_gallons_needed * (cookies_needed / cookies_baked)
     return result

print(solution())