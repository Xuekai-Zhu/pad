def solution():
    """Allison went to the craft store with her friend Marie to buy some glue sticks and construction paper. Allison bought 8 more glue sticks than Marie, but Marie bought six times as many packs of construction paper as Allison. If Marie bought 15 glue sticks and 30 packs of construction paper how many craft supply items did Allison buy all together?"""
    # Define the number of glue sticks Marie bought
    marie_glue_sticks = 15

    # Define the number of packs of construction paper Marie bought
    marie_construction_paper_packs = 30

    # Calculate the number of glue sticks Allison bought
    allison_glue_sticks = marie_glue_sticks + 8

    # Calculate the number of packs of construction paper Allison bought
    allison_construction_paper_packs = marie_construction_paper_packs / 6

    # Calculate the total number of craft supply items Allison bought
    total_items = allison_glue_sticks + allison_construction_paper_packs

    # Display the total number of craft supply items Allison bought
    result = total_items
    return result

print(solution())