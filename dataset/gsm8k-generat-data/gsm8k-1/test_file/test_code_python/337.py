def solution():
    """A pink frog weighs the same as a blue beetle, the same as a green toad, 10 pounds less than a yellow snake, but 20 pounds more than a red bird. If the pink frog weighs 50 pounds, calculate the total weight of a container carrying one of each animal if the container also weighs 20 pounds."""
    pink_frog_weight = 50
    blue_beetle_weight = pink_frog_weight
    green_toad_weight = pink_frog_weight
    yellow_snake_weight = pink_frog_weight + 10
    red_bird_weight = pink_frog_weight - 20
    container_weight = 20
    total_weight = pink_frog_weight + blue_beetle_weight + green_toad_weight + yellow_snake_weight + red_bird_weight + container_weight
    result = total_weight
    return result

print(solution())