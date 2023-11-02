def solution():
    # Find the number of jars of plum jelly sold
    plum_jelly = 6

    # Find the number of jars of raspberry jelly sold
    raspberry_jelly = (1/3) * grape_jelly

    # Find the number of jars of grape jelly sold
    grape_jelly = 2 * strawberry_jelly
    total_jelly = plum_jelly + strawberry_jelly + grape_jelly + raspberry_jelly

    # Calculate the number of jars of strawberry jelly sold
    strawberry_jelly = (total_jelly - plum_jelly - grape_jelly - raspberry_jelly) / 2

    result = strawberry_jelly
    return result

print(solution())