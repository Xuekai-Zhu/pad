def solution():
    # Calculate the total weight of laundry
    total_weight = (20/4) + (20/2)  # 20 shirts weigh 5 pounds (20/4) and 20 pants weigh 10 pounds (20/2)

    # Calculate the number of loads of laundry
    num_loads = total_weight / 5  # Jon's laundry machine can do 5 pounds of laundry at a time
    result = num_loads
    return result

print(solution())