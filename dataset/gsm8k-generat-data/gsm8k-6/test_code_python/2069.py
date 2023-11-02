def solution():
    # Calculate the number of shoes Page donates
    donated_shoes = round(0.3 * 80)  # she donates 30% of her collection

    # Calculate Page's new shoe collection after the donation and purchasing 6 more pairs
    new_collection = (80 - donated_shoes) + 6

    result = new_collection
    return result

print(solution())