def solution():
    # Calculate the total number of eggs brought to the party
    kelsey_eggs = (2/5) * 30  # 30 eggs in a tray
    stephanie_eggs = 0.5 * 30
    alayah_eggs = (kelsey_eggs + stephanie_eggs + 40)
    total_eggs = kelsey_eggs + stephanie_eggs + alayah_eggs

    # Calculate the total number of eggs used at the party
    used_eggs = total_eggs - (2 * 30)  # Willa already had 2 trays
    result = used_eggs
    return result

print(solution())