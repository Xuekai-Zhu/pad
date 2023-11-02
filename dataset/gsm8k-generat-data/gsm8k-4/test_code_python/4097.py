def solution():
    """At a party, there are 400 students, a combination of poets, singers and tree huggers. There are 50 more poets than treehuggers at the party. If the number of tree huggers is 120, how many singers are at the party?"""
    # Define the number of tree huggers and poets
    tree_huggers = 120
    poets = tree_huggers + 50

    # Calculate the number of singers
    singers = 400 - tree_huggers - poets

    # Return the result
    result = singers
    return result

print(solution())