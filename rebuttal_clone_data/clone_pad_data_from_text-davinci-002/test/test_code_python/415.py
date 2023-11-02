def solution():
    money_given = 40
    poster_cost = 5
    notebook_cost = 4
    bookmark_cost = 2
    posters_bought = 2
    notebooks_bought = 3
    bookmarks_bought = 2
    total_cost = (poster_cost * posters_bought) + (notebook_cost * notebooks_bought) + (bookmark_cost * bookmarks_bought)
    money_left = money_given - total_cost
    result = money_left
    return result

print(solution())