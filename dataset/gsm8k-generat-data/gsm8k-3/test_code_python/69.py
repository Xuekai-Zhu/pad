def solution():
    """Carly collected 7 starfish with 5 arms each and one seastar with 14 arms. How many arms do the animals she collected have in total?"""
    # Define the number of starfish and seastars
    num_starfish = 7
    num_seastars = 1

    # Define the number of arms per starfish and seastar
    starfish_arms = 5
    seastar_arms = 14

    # Calculate the total number of arms
    total_arms = (num_starfish * starfish_arms) + (num_seastars * seastar_arms)

    # return the result
    result = total_arms
    return result

print(solution())