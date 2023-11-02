def solution():
    bruise_causing = "blunt trauma"
    touching_required = False
    if bruise_causing not in reiki and not touching_required:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())