def solution():
    total_oranges = 7 * 12  # Mr. Salazar had 7 dozen oranges
    reserved_oranges = total_oranges * (1 / 4)  # He reserved 1/4 of the oranges for his friend
    remaining_oranges = total_oranges - reserved_oranges  # He has the remaining oranges left
    sold_yesterday = remaining_oranges * (3 / 7)  # He sold 3/7 of the remaining oranges yesterday
    remaining_oranges -= sold_yesterday  # He now has fewer oranges left
    remaining_oranges -= 4  # He saw 4 rotten oranges today

    result = remaining_oranges
    return result

print(solution())