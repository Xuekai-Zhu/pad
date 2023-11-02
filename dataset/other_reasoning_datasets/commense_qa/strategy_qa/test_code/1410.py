def solution():
    gospel_album_sales = 200
    pop_album_sales = 800000
    if gospel_album_sales < pop_album_sales:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())