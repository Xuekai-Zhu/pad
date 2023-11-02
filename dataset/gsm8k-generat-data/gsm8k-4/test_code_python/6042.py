def solution():
    """Allison went to the craft store with her friend Marie to buy some glue sticks and construction paper. Allison bought 8 more glue sticks than Marie, but Marie bought six times as many packs of construction paper as Allison. If Marie bought 15 glue sticks and 30 packs of construction paper how many craft supply items did Allison buy all together?"""
    # Define the number of glue sticks bought by Marie
    marie_glue = 15

    # Calculate the number of glue sticks bought by Allison
    allison_glue = marie_glue + 8

    # Define the number of packs of construction paper bought by Marie
    marie_paper = 30

    # Calculate the number of packs of construction paper bought by Allison
    allison_paper = allison_glue * 6

    # Calculate the total number of craft supplies bought by Allison
    total_supplies = allison_glue + allison_paper

    # return the result
    result = total_supplies
    return result

print(solution())