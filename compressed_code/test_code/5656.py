def solution():
    
    aaron_scarves = 10
    aaron_sweaters = 5
    enid_sweaters = 8
    scarf_wool = 3
    sweater_wool = 4
    total_scarf_wool = aaron_scarves * scarf_wool
    total_sweater_wool = (aaron_sweaters + enid_sweaters) * sweater_wool
    total_wool = total_scarf_wool + total_sweater_wool
    result = total_wool
    return result

print(solution())