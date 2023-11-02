def solution():
    
    total_students = 400
    tree_huggers = 120
    poets = tree_huggers + 50
    singers = total_students - (tree_huggers + poets)
    result = singers
    return result

print(solution())