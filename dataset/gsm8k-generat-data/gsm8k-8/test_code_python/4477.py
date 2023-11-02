def solution():
    # Define the total number of brownies
    total_brownies = 10 * 20

    # Calculate the number of brownies set aside for the bake sale
    bake_sale_brownies = total_brownies * (3/4)

    # Calculate the remaining brownies
    remaining_brownies = total_brownies - bake_sale_brownies

    # Calculate the number of brownies put in the container
    container_brownies = remaining_brownies * (3/5)

    # Calculate the number of brownies given out
    given_out_brownies = remaining_brownies - container_brownies

    result = given_out_brownies
    return result

print(solution())