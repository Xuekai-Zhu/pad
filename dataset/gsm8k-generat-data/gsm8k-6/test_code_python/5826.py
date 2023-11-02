def solution():
    # Calculate the total number of animals running through the field
    cats = 4
    rabbits = cats * 2
    hares = rabbits * 3
    total_animals = 1 + cats + rabbits + hares  # 1 dog joins the group of cats
    result = total_animals
    return result

print(solution())