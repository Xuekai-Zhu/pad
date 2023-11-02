def solution():
    # Calculate the number of animals that made it to the shore
    sheep_alive = 20 - 3  # 3 of the sheep drowned
    cows_alive = 10 - 2*3  # Twice as many cows drowned as did sheep
    dogs_alive = 14  # All of the dogs made it to shore
    total_animals = sheep_alive + cows_alive + dogs_alive
    result = total_animals
    return result

print(solution())