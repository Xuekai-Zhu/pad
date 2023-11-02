def solution():
    # Calculate the total amount of popcorn needed
    total_popcorn = 3 + 4 + 6 + 3  # Joanie wants 3 cups, Mitchell wants 4 cups, Miles and Davis split 6 cups, Cliff wants 3 cups

    # Calculate the amount of popcorn kernels needed to make the total amount of popcorn
    kernels_needed = (total_popcorn / 4) * 2  # 2 tablespoons of kernels make 4 cups of popcorn

    result = kernels_needed
    return result

print(solution())