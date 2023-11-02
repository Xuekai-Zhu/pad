def solution():
    num_containers = 5
    num_pencils = 150
    additional_pencils = 30

    # Add the additional pencils to the total number
    total_pencils = num_pencils + additional_pencils

    # Divide the total number of pencils evenly between the containers
    pencils_per_container = total_pencils / num_containers

    result = pencils_per_container
    return result

print(solution())