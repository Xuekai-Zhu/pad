def solution():
    tray_capacity = 30  # Each tray can hold 30 eggs
    kelsey_tray = 2/5  # Kelsey brought 2/5 of a tray of eggs
    stephanie_tray = 1/2  # Stephanie brought half a tray of eggs
    kelsey_stephanie_total = kelsey_tray + stephanie_tray  # Kelsey and Stephanie brought this many trays in total
    alayah_total = kelsey_stephanie_total + 40/30  # Alayah brought 40 more eggs than Kelsey and Stephanie combined, with each tray holding 30 eggs
    willa_total = 2 * tray_capacity  # Willa had two trays of eggs

    # Calculate the total number of eggs used at the party
    total_eggs = int((kelsey_tray + stephanie_tray + alayah_total) * tray_capacity + willa_total)
    result = total_eggs
    return result

print(solution())