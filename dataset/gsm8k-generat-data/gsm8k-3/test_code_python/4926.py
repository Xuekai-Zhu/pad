def solution():
    """Heath spent his weekend helping at his uncle’s farm planting carrots. He planted 400 rows of carrots with 300 plants in each row. He used a machine to get the planting done and it took him 20 hours. How many carrots did he plant each hour?"""
    # Define the number of rows planted and the number of plants per row
    rows_planted = 400
    plants_per_row = 300

    # Calculate the total number of carrots planted
    total_plants = rows_planted * plants_per_row

    # Calculate the number of carrots planted per hour
    plants_per_hour = total_plants / 20

    # Display the number of carrots planted per hour
    result = plants_per_hour
    return result

print(solution())