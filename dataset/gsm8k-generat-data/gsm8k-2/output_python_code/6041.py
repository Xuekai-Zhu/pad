def solution():
    """Allison went to the craft store with her friend Marie to buy some glue sticks and construction paper. Allison bought 8 more glue sticks than Marie, but Marie bought six times as many packs of construction paper as Allison. If Marie bought 15 glue sticks and 30 packs of construction paper how many craft supply items did Allison buy all together?"""
    marie_glue_sticks = 15
    marie_paper_packs = 30
    allison_glue_sticks = marie_glue_sticks + 8
    allison_paper_packs = allison_glue_sticks * 6
    total_items = allison_glue_sticks + allison_paper_packs
    result = total_items
    return result

print(solution())