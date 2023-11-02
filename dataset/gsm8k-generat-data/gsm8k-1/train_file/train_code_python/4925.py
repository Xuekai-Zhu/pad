def solution():
    """Heath spent his weekend helping at his uncle’s farm planting carrots. He planted 400 rows of carrots with 300 plants in each row. He used a machine to get the planting done and it took him 20 hours. How many carrots did he plant each hour?"""
    rows_planted = 400
    plants_per_row = 300
    total_plants = rows_planted * plants_per_row
    hours_worked = 20
    plants_per_hour = total_plants / hours_worked
    result = plants_per_hour
    return result

print(solution())