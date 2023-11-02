def solution():
    # Calculate the number of alive tomato plants
    alive_tomato_plants = 6 // 2

    # Calculate the number of alive pepper plants
    alive_pepper_plants = 4 // 2 - 1

    # Calculate the total number of vegetables Shanna will harvest
    total_vegetables = (alive_tomato_plants + 2 + alive_pepper_plants) * 7

    result = total_vegetables
    return result

print(solution())