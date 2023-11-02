def solution():
    persian_cats_jaime = 4
    maine_coon_cats_jaime = 2
    persian_cats_gordon = persian_cats_jaime / 2
    maine_coon_cats_gordon = maine_coon_cats_jaime + 1
    maine_coon_cats_hawkeye = maine_coon_cats_gordon - 1
    total_cats = persian_cats_jaime + maine_coon_cats_jaime + persian_cats_gordon + maine_coon_cats_gordon + maine_coon_cats_hawkeye
    result = total_cats
    
    return result

print(solution())