def solution():
    """Grandma left $124,600 in her will. She gave half of it to her favorite grandchild, Shelby. The rest was to be evenly divided among the remaining 10 grandchildren. How many dollars did one of the remaining 10 grandchildren receive?"""
    inheritance = 124600
    shelby_share = inheritance / 2
    remaining_share = inheritance - shelby_share
    grandchildren_count = 10
    each_grandchild_share = remaining_share / grandchildren_count
    result = each_grandchild_share
    return result

print(solution())