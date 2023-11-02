def solution():
    banana_tree_type = "monocot"
    gavel_material = "hardwood"
    dicot_trees = ["oak", "maple", "sycamore"]
    if banana_tree_type != "dicot" and gavel_material in dicot_trees:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())