def solution():
    """Juan needs 10 half-gallons of milk to bake 40 cookies with. How many half-gallons of milk does Juan need to bake 200 dozen cookies?"""
    cookies_per_half_gallon = 40/10 # 4 cookies per half-gallon
    total_cookies = 200 * 12 # 2400 cookies
    half_gallons_needed = total_cookies / cookies_per_half_gallon / 2 # divide by 2 to account for half-gallons
    result = half_gallons_needed
    return result

print(solution())