def solution():
    # Define the ratios of jelly sales
    grape_to_strawberry = 2
    raspberry_to_plum = 2
    raspberry_to_grape = 1/3

    # Calculate the sales of plum jelly
    plum_sales = 6

    # Calculate the sales of raspberry jelly
    raspberry_sales = plum_sales * raspberry_to_plum

    # Calculate the sales of grape jelly
    grape_sales = raspberry_sales / raspberry_to_grape

    # Calculate the sales of strawberry jelly
    strawberry_sales = grape_sales / grape_to_strawberry
    result = strawberry_sales
    return result

print(solution())