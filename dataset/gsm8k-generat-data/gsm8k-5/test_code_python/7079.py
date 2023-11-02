def solution():
    total_pencils = 150 + 30  # Eric has a total of 180 colored pencils
    num_containers = 5  # Eric needs to distribute the pencils evenly between 5 containers

    # Calculate how many pencils can be evenly distributed between the containers
    even_pencils = total_pencils // num_containers

    result = even_pencils
    return result

print(solution())