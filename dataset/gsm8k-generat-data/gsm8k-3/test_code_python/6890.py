def solution():
    """Christopher, Jameson, and June each bought a toy sword. June's sword is 5 inches longer than Jameson's sword. Jameson's sword is 3 inches longer than twice the length of Christopher's sword. Christopher's sword is 15 inches long. How many inches longer is June's sword than Christopher's sword?"""
    # Define the length of Christopher's sword
    chris_length = 15

    # Calculate the length of Jameson's sword
    james_length = 2 * chris_length + 3

    # Calculate the length of June's sword
    june_length = james_length + 5

    # Calculate the difference in length between June's and Christopher's sword
    difference = june_length - chris_length

    # Display the difference in length
    result = difference
    return result

print(solution())