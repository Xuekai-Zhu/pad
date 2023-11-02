def solution():
    """At a party, there are 400 students, a combination of poets, singers and tree huggers. There are 50 more poets than treehuggers at the party. If the number of tree huggers is 120, how many singers are at the party?"""
    # Define the number of tree huggers and poets
    treehuggers = 120
    poets = treehuggers + 50

    # Calculate the number of singers
    singers = 400 - (treehuggers + poets)

    # Display the number of singers
    result = singers
    return result

print(solution())