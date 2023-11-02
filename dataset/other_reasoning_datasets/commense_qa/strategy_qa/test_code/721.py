def solution():
    # Define the two topics
    cell_biology = "structure and function of cells"
    al_qaeda_cells = "small groups of terrorists acting semi-independently"
    # Check if cell biology teaches about Al Qaeda's life cycle
    if al_qaeda_cells not in cell_biology:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())