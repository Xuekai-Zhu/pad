def solution():
    # Find the number of glue sticks Allison bought
    glue_sticks_allison = 15 - 8  # Allison bought 8 more glue sticks than Marie, who bought 15
    # Find the number of packs of construction paper Allison bought
    paper_allison = 30 / 6  # Marie bought six times as many packs of construction paper as Allison
    # Calculate the total number of craft supply items Allison bought
    total_items_allison = glue_sticks_allison + paper_allison
    result = total_items_allison
    return result

print(solution())