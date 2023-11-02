def solution():
    """On the first day of the garden center sale, 14 marigolds were sold. The next day 25 more marigolds were sold. On the third day the center sold two times the number of marigolds it did on the day before. How many marigolds were sold during the sale?"""
    day1 = 14
    day2 = day1 + 25
    day3 = day2 * 2
    total = day1 + day2 + day3
    result = total
    return result

print(solution())