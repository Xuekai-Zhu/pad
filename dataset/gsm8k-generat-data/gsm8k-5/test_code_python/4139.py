def solution():
    eric_throwing_stars = 4
    chad_throwing_stars = eric_throwing_stars * 2
    chad_throwing_stars -= 2  # Jeff bought 2 from Chad
    jeff_throwing_stars = 6
    total_throwing_stars = eric_throwing_stars + chad_throwing_stars + jeff_throwing_stars
    result = total_throwing_stars
    return result

print(solution())