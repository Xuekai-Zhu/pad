def solution():
    # Calculate the number of months it takes for the grass to grow from 2 to 4 inches
    months_to_grow = (4-2) / 0.5  # grass grows by 0.5 inches per month
    # Calculate the number of times John cuts his grass per year
    times_to_cut = 12 / months_to_grow
    # Calculate the cost per cut and the total cost per year 
    cost_per_cut = 100
    total_cost = cost_per_cut * times_to_cut
    result = total_cost
    return result

print(solution())