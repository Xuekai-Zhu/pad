def solution():
    # Calculate the percentage taller of each crane
    crane1_percentage = ((228-200)/200) * 100
    crane2_percentage = ((120-100)/100) * 100
    crane3_percentage = ((147-140)/140) * 100

    # Calculate the average percentage taller of all cranes
    average_percentage = (crane1_percentage + crane2_percentage + crane3_percentage) / 3
    result = average_percentage
    return result

print(solution())