def solution():
    marie_glue_sticks = 15
    marie_construction_paper_packs = 30

    # Allison bought 8 more glue sticks than Marie
    allison_glue_sticks = marie_glue_sticks + 8

    # Marie bought six times as many packs of construction paper as Allison
    allison_construction_paper_packs = marie_construction_paper_packs / 6

    # Calculate the total number of craft supply items Allison bought
    total_items = allison_glue_sticks + allison_construction_paper_packs
    result = total_items
    return result

print(solution())