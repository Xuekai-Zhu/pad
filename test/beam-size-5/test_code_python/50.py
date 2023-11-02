def solution():
    
    # Define the initial number of kittens
    initial_kittens = 7

    # Define the number of kittens adopted by the first cat
    patchy_kittens = 3 * initial_kittens

    # Define the number of kittens adopted by the second cat
    trixie_kittens = 12

    # Calculate the total number of kittens
    total_kittens = initial_kittens + patchy_kittens + trixie_kittens

    # Display the total number of kittens
    result = total_kittens
    return result

print(solution())