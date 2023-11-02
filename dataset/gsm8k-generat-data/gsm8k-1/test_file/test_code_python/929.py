def solution():
    """A charity group decides to do a yard sale. 10 people donate 5 boxes of stuff each. They also have 10 boxes of stuff already. They can fit 2 boxes worth of stuff per table. If they already own 15 tables, how many new tables do they need?"""
    total_people = 10
    boxes_per_person = 5
    total_boxes = total_people * boxes_per_person + 10
    boxes_per_table = 2
    total_tables_needed = (total_boxes // boxes_per_table) - 15
    result = total_tables_needed
    
    return result

print(solution())