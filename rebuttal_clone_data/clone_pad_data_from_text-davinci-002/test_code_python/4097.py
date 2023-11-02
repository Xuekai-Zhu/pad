def solution():
    total_students = 400
    poets = total_students / 2 + total_students / 4
    tree_huggers = total_students / 4
    singers = total_students - poets - tree_huggers
    result = singers
    return result

print(solution())