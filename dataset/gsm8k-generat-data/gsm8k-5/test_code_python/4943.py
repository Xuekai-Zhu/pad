def solution():
    # Juan needs 10 half-gallons of milk to bake 40 cookies, so he needs 1/4 of a half-gallon for every 10 cookies
    milk_per_cookie = 1/4

    # Juan wants to bake 200 dozen cookies, which is 2400 cookies in total
    total_cookies = 2400

    # Calculate how much milk Juan needs to bake 2400 cookies
    milk_needed = milk_per_cookie * total_cookies

    # Calculate how many half-gallons of milk Juan needs
    half_gallons_needed = milk_needed / 0.5

    result = half_gallons_needed
    return result

print(solution())