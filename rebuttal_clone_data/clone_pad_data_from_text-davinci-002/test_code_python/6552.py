def solution():
    grape_jelly = 2
    strawberry_jelly = 1
    raspberry_jelly = 2 / 3 
    plum_jelly = 1 / 3
    total_jelly = grape_jelly + strawberry_jelly + raspberry_jelly + plum_jelly
    sold_plum_jelly = 6
    sold_strawberry_jelly = sold_plum_jelly / total_jelly
    result = sold_strawberry_jelly
    return result

print(solution())