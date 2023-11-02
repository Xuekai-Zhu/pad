def solution():
    """Allison went to the craft store with her friend Marie to buy some glue sticks and construction paper. Allison bought 8 more glue sticks than Marie, but Marie bought six times as many packs of construction paper as Allison. If Marie bought 15 glue sticks and 30 packs of construction paper how many craft supply items did Allison buy all together?"""
    marie_glue_sticks = 15
    allison_glue_sticks = marie_glue_sticks + 8
    marie_construction_paper = 30
    allison_construction_paper = marie_construction_paper / 6
    total_items = allison_glue_sticks + allison_construction_paper
    result = total_items
    return result

print(solution())