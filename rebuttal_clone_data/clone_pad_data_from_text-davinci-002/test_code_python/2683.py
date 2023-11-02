def solution():
    
    magazines_bought_on_friday = 8
    magazines_bought_on_saturday = 12
    magazines_bought_on_sunday = magazines_bought_on_friday * 4
    magazines_chewed_up_by_dog = 4
    total_magazines = magazines_bought_on_friday + magazines_bought_on_saturday + magazines_bought_on_sunday - magazines_chewed_up_by_dog
    result = total_magazines
    return result

print(solution())