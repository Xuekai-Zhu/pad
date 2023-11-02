def solution():
    """When Michelle makes fresh pasta, she first makes the dough, then she rolls it out and cuts it, and then she hangs it on racks to dry for cooking later. She needs a drying rack for each three pounds of pasta she makes, and it takes two cups of flour to make each pound of pasta dough. She owns three racks right now. How many more drying racks will Michelle need if she makes pasta using three 8-cup bags of flour?"""
    flour_per_pound = 2
    pounds_of_pasta = 3 * 3
    drying_racks_needed = (pounds_of_pasta // 3) - 3
    result = drying_racks_needed
    return result

print(solution())