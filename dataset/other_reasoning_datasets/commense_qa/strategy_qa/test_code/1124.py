def solution():
    mary_queen_of_scots_descendants = ["James I", "Charles I"]
    gunpowder_plot_eliminated_descendants = False
    for descendant in mary_queen_of_scots_descendants:
        if descendant in ["Guy Fawkes", "Robert Catesby", "Thomas Percy"]:
            gunpowder_plot_eliminated_descendants = True
            break
    if gunpowder_plot_eliminated_descendants:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())