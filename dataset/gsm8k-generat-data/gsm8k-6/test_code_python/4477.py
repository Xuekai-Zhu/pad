def solution():
    # Calculate the total number of brownies baked
    total_brownies = 10 * 20  # 10 batches of 20 brownies each

    # Calculate the number of brownies set aside for the bake sale
    bake_sale_brownies = (3/4) * total_brownies

    # Calculate the number of brownies remaining after the bake sale
    remaining_brownies = total_brownies - bake_sale_brownies

    # Calculate the number of brownies put in the container
    container_brownies = (3/5) * remaining_brownies

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies

    result = given_out_brownies
    return result

print(solution())