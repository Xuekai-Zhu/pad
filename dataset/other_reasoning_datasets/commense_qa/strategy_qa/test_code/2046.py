def solution():
    pope_name = "Alexander VI"
    pope_descendants = ["Juan Borgia", "Francis Borgia"]
    saint_descendants = ["Francis Borgia"]
    if any(descendant in saint_descendants for descendant in pope_descendants):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())