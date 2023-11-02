def solution():
    color_green_influence = True
    famous_book = "Green Eggs and Ham"
    if color_green_influence and famous_book.startswith("Green"):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())