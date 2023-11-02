def solution():
    tmnt_animated_series_food = "pizza"
    tmnt_coloring_book_food = ["pizza"]
    if tmnt_animated_series_food in tmnt_coloring_book_food:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())