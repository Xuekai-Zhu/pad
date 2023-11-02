def solution():
    # Let x be the number of cookies Kenny has
    x = 2 * 24  # Chris has half as many cookies as Kenny, and Kenny has 24, so Chris has 12
    # Glenn has four times as many cookies as Kenny, and Kenny has x, so Glenn has 4*x=96

    # Total number of cookies
    total_cookies = x + 12 + 24

    result = total_cookies
    return result

print(solution())