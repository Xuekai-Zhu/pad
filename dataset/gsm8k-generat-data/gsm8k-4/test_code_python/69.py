def solution():
    """Carly collected 7 starfish with 5 arms each and one seastar with 14 arms. How many arms do the animals she collected have in total?"""
    # Define the number of arms on each type of animal
    starfish_arms = 5
    seastar_arms = 14

    # Calculate the total number of arms on the starfish
    total_starfish_arms = 7 * starfish_arms

    # Calculate the total number of arms on all the animals
    total_arms = total_starfish_arms + seastar_arms

    # return the result
    result = total_arms
    return result

print(solution())