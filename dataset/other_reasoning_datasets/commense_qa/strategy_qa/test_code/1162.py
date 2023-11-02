def solution():
    black_album_sales = 20000000
    post_1996_album_sales = 14000000
    if post_1996_album_sales < black_album_sales:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())