def solution():
    # Define the number of glue sticks Marie bought
    marie_glue_sticks = 15

    # Calculate how many glue sticks Allison bought
    allison_glue_sticks = marie_glue_sticks + 8

    # Define the number of packs of construction paper Marie bought
    marie_construction_paper = 30

    # Calculate how many packs of construction paper Allison bought
    allison_construction_paper = marie_construction_paper / 6

    # Calculate the total number of craft supply items Allison bought
    total_items = allison_glue_sticks + allison_construction_paper
    result = total_items
    return result

print(solution())