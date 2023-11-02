def solution():
    # Define the initial number of brownies
    initial_brownies = 20

    # Calculate the number of brownies Annie gave to the administrator
    admin_brownies = initial_brownies / 2

    # Calculate the number of brownies remaining after the administrator takes their share
    remaining_brownies = initial_brownies - admin_brownies

    # Calculate the number of brownies Annie gave Carl
    carl_brownies = remaining_brownies / 2

    # Calculate the number of brownies remaining after Carl and Simon get their share
    final_brownies = remaining_brownies - carl_brownies - 2
    result = final_brownies
    return result

print(solution())