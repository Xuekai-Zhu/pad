def solution():
    """Mary is chopping up some old furniture to make firewood. Chairs make 6 sticks of wood, tables make 9 sticks of wood, and stools make 2 sticks of wood. Mary needs to burn 5 sticks of wood per hour to stay warm. If Mary chops up 18 chairs, 6 tables and 4 stools, how many hours can she keep warm?"""
    chairs = 18
    tables = 6
    stools = 4
    sticks_per_chair = 6
    sticks_per_table = 9
    sticks_per_stool = 2
    sticks = (chairs * sticks_per_chair) + (tables * sticks_per_table) + (stools * sticks_per_stool)
    hours = sticks / 5
    result = hours
    return result

print(solution())