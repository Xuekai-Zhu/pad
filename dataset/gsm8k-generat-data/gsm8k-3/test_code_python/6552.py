def solution():
    """A grocery store has 4 kinds of jelly. They sell grape jelly twice as much as strawberry jelly, and raspberry jelly twice as much as plum jelly. The raspberry jelly sells a third as much as the grape jelly. If they sold 6 jars of plum jelly today, how many jars of strawberry jelly did they sell?"""
    # Define the ratios of jelly sales
    STRAWBERRY_RATIO = 1
    GRAPE_RATIO = 2
    RASPBERRY_RATIO = 1/3
    PLUM_RATIO = 1

    # Define the number of plum jelly jars sold today
    plum_jelly_sold = 6

    # Calculate the ratio of strawberry jelly sales to plum jelly sales
    ratio_strawberry_to_plum = STRAWBERRY_RATIO / PLUM_RATIO

    # Calculate the ratio of grape jelly sales to plum jelly sales
    ratio_grape_to_plum = GRAPE_RATIO / PLUM_RATIO

    # Calculate the ratio of raspberry jelly sales to plum jelly sales
    ratio_raspberry_to_plum = RASPBERRY_RATIO / PLUM_RATIO

    # Calculate the number of grape jelly jars sold today
    grape_jelly_sold = ratio_grape_to_plum * plum_jelly_sold

    # Calculate the number of raspberry jelly jars sold today
    raspberry_jelly_sold = ratio_raspberry_to_plum * plum_jelly_sold

    # Calculate the number of strawberry jelly jars sold today
    strawberry_jelly_sold = ratio_strawberry_to_plum * plum_jelly_sold

    # Display the number of strawberry jelly jars sold today
    result = strawberry_jelly_sold
    return result

print(solution())