def solution():
    plum_jelly = 6  # They sold 6 jars of plum jelly today
    grape_jelly = 2 * strawberry_jelly  # They sell grape jelly twice as much as strawberry jelly
    raspberry_jelly = 2 * plum_jelly  # They sell raspberry jelly twice as much as plum jelly
    raspberry_jelly_sales = grape_jelly / 3  # The raspberry jelly sells a third as much as the grape jelly

    # Calculate the total number of jelly jars sold
    total_jelly = plum_jelly + grape_jelly + raspberry_jelly + raspberry_jelly_sales

    # Calculate the number of jars of strawberry jelly sold
    strawberry_jelly = (total_jelly - plum_jelly - grape_jelly - raspberry_jelly_sales) / 2
    result = strawberry_jelly
    return result

print(solution())