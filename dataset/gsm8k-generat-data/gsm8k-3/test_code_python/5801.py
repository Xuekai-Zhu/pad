def solution():
    """Aubree saw 20 beavers and 40 chipmunks by a tree when going to school and scared them away when they saw her. While coming back from school, she realized the number of beavers had doubled and the number of chipmunks had decreased by 10. What's the total number of animals she saw that day?"""
    # Define the number of beavers and chipmunks Aubree saw on her way to school
    beavers1 = 20
    chipmunks1 = 40

    # Define the number of beavers and chipmunks Aubree saw on her way back from school
    beavers2 = beavers1 * 2
    chipmunks2 = chipmunks1 - 10

    # Calculate the total number of animals Aubree saw that day
    total_animals = beavers1 + chipmunks1 + beavers2 + chipmunks2

    # Display the total number of animals
    result = total_animals
    return result

print(solution())