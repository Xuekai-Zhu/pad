def solution():
    plum_jelly_sold = 6
    
    # Find the ratio of sales for each jelly type
    grape_to_strawberry = 2
    raspberry_to_plum = 2
    raspberry_to_grape = 1/3

    # Use the ratio to find the number of jars sold for each jelly type
    plum_sold = plum_jelly_sold
    raspberry_sold = raspberry_to_plum * plum_sold
    grape_sold = grape_to_strawberry * strawberry_sold = 2 * 2 * raspberry_sold
    strawberry_sold = grape_sold / grape_to_strawberry

    result = strawberry_sold
    return result

print(solution())