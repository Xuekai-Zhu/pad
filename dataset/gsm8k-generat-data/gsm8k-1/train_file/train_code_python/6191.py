def solution():
    """Greg and Sarah have 18 apples that they are going to split evenly. Susan has twice as many apples as Greg will end up with. Mark has 5 fewer apples than Susan. Their mom needs 40 apples to make an apple pie. How many will she have left over?"""
    total_apples = 18
    greg_apples = total_apples / 2
    susan_apples = greg_apples * 2
    mark_apples = susan_apples - 5
    mom_need = 40
    total_people = 4
    apples_leftover = total_apples - (greg_apples + susan_apples + mark_apples + mom_need)
    result = apples_leftover
    return result

print(solution())