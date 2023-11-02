def solution():
    num_batches = 10
    brownies_per_batch = 20
    sale_percentage = 0.75
    container_percentage = 0.6

    # Calculate the total number of brownies baked
    total_brownies = num_batches * brownies_per_batch

    # Calculate the number of brownies set aside for the bake sale
    sale_brownies = total_brownies * sale_percentage

    # Calculate the number of brownies remaining after the bake sale
    remaining_brownies = total_brownies - sale_brownies

    # Calculate the number of brownies put in the container
    container_brownies = remaining_brownies * container_percentage

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies
    result = given_out_brownies
    return result

print(solution())