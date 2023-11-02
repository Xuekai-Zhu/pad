def solution():
    num_posters = 2
    poster_price = 5

    num_notebooks = 3
    notebook_price = 4

    num_bookmarks = 2
    bookmark_price = 2

    total_spent = (num_posters * poster_price) + (num_notebooks * notebook_price) + (num_bookmarks * bookmark_price)
    remaining_money = (2 * 20) - total_spent
    result = remaining_money
    return result

print(solution())