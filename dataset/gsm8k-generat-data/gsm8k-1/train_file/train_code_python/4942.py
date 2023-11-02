def solution():
    """Juan needs 10 half-gallons of milk to bake 40 cookies with. How many half-gallons of milk does Juan need to bake 200 dozen cookies?"""
    cookies_per_half_gallon = 40
    half_gallons_needed = 10
    cookies_needed = 200 * 12
    half_gallons_needed_new = (cookies_needed / cookies_per_half_gallon) * (half_gallons_needed / 10)
    result = half_gallons_needed_new
    return result

print(solution())