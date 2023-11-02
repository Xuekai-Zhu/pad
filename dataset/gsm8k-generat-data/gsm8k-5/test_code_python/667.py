def solution():
    # Calculate the total number of dogs
    total_dogs = 2 * 15  # Half the dogs have spots, so there are 2 spots per dog

    # Calculate the number of dogs with pointy ears
    pointy_ear_dogs = total_dogs / 5  # 1/5 of the dogs have pointy ears

    result = pointy_ear_dogs
    return result

print(solution())