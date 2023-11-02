def solution():
    popcorn_per_tablespoon = 4 / 2  # Two tablespoons of kernels make 4 cups of popcorn
    joanie_popcorn = 3  # Joanie wants 3 cups of popcorn
    mitchell_popcorn = 4  # Mitchell wants 4 cups of popcorn
    miles_davis_popcorn = 6  # Miles and Davis will split 6 cups of popcorn
    cliff_popcorn = 3  # Cliff will eat 3 cups of popcorn

    # Calculate the total popcorn needed
    total_popcorn = joanie_popcorn + mitchell_popcorn + miles_davis_popcorn + cliff_popcorn

    # Calculate the total number of tablespoons needed
    total_tablespoons = total_popcorn / popcorn_per_tablespoon
    result = total_tablespoons
    return result

print(solution())