def solution():
    # Define the historical and religious context of the conflict
    muslim_holy_sites = ["Mecca", "Medina", "Jerusalem"]
    ottoman_occupation = True
    muslim_desire_to_reclaim_holy_lands = True
    # Check if the Muslim world is hostile to Israel
    if "Jerusalem" in muslim_holy_sites and ottoman_occupation and muslim_desire_to_reclaim_holy_lands:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())