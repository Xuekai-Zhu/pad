def solution():
    # Define the initial number of pencils per container
    pencils_per_container = 150 / 5

    # Calculate the new total number of pencils
    total_pencils = 150 + 30

    # Calculate the new number of pencils per container
    new_pencils_per_container = total_pencils / 5

    # Calculate the number of pencils that can be evenly distributed between the containers
    evenly_distributable_pencils = new_pencils_per_container - pencils_per_container

    result = evenly_distributable_pencils
    return result

print(solution())