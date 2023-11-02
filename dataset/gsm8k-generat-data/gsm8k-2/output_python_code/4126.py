def solution():
    """Daisy's Flower Shop sold 45 daisies on its first day. On their second day, they sold 20 more flowers than they did on their first day. On the third day, they sold 10 less than twice the flowers that were sold than on the second day. If the flower shop sold a total of 350 daisies for 4 days, how many daisies were sold on the 4th day?"""
    day1 = 45
    day2 = day1 + 20
    day3 = 2 * day2 - 10
    total_daisies = day1 + day2 + day3
    day4 = 350 - total_daisies
    result = day4
    return result

print(solution())