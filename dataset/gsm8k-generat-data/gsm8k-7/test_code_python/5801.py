def solution():
    initial_beavers = 20
    initial_chipmunks = 40

    # Calculate the total number of animals Aubree saw initially
    total_initial_animals = initial_beavers + initial_chipmunks

    # Calculate the number of beavers Aubree saw on her way back from school
    final_beavers = initial_beavers * 2

    # Calculate the number of chipmunks Aubree saw on her way back from school
    final_chipmunks = initial_chipmunks - 10

    # Calculate the total number of animals Aubree saw on her way back from school
    total_final_animals = final_beavers + final_chipmunks

    # Calculate the total number of animals Aubree saw that day
    total_animals = total_initial_animals + total_final_animals
    result = total_animals
    return result

print(solution())