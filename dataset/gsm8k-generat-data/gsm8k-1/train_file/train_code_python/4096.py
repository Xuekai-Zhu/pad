def solution():
    """At a party, there are 400 students, a combination of poets, singers and tree huggers. There are 50 more poets than treehuggers at the party. If the number of tree huggers is 120, how many singers are at the party?"""
    total_students = 400
    tree_huggers = 120
    poets = tree_huggers + 50
    singers = total_students - (tree_huggers + poets)
    result = singers
    return result

print(solution())