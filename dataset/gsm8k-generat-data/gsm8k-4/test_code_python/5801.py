def solution():
    """Aubree saw 20 beavers and 40 chipmunks by a tree when going to school and scared them away when they saw her. While coming back from school, she realized the number of beavers had doubled and the number of chipmunks had decreased by 10. What's the total number of animals she saw that day?"""
    # Define the initial number of beavers and chipmunks
    initial_beavers = 20
    initial_chipmunks = 40

    # Calculate the final number of beavers and chipmunks
    final_beavers = initial_beavers * 2
    final_chipmunks = initial_chipmunks - 10

    # Calculate the total number of animals she saw that day
    total_animals = initial_beavers + initial_chipmunks + final_beavers + final_chipmunks

    # return the result
    result = total_animals
    return result

print(solution())