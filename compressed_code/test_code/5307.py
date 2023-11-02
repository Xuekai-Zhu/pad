def solution():
    
    pieces_per_log = 5
    logs_per_tree = 4
    total_pieces = 500
    pieces_per_tree = logs_per_tree * pieces_per_log
    trees_chopped = total_pieces / pieces_per_tree
    result = trees_chopped
    return result

print(solution())