def solution():
    
    # Define the number of 2-legged animals and the number of 4-legged animals
    num_2legged_animals = 10
    num_4legged_animals = 15

    # Calculate the total number of pairs of animal legs
    total_legs = (num_2legged_animals * 2) + (num_4legged_animals * 4)

    # Display the total number of pairs of animal legs
    result = total_legs
    return result

print(solution())