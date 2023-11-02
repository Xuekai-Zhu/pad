def solution():
    """Mary is chopping up some old furniture to make firewood. Chairs make 6 sticks of wood, tables make 9 sticks of wood, and stools make 2 sticks of wood. Mary needs to burn 5 sticks of wood per hour to stay warm. If Mary chops up 18 chairs, 6 tables and 4 stools, how many hours can she keep warm?"""
    chairs = 6
    tables = 9
    stools = 2
    sticks_needed_per_hour = 5
    total_sticks = (chairs * 18) + (tables * 6) + (stools * 4)
    hours_warm = total_sticks / sticks_needed_per_hour
    result = hours_warm
    return result

print(solution())