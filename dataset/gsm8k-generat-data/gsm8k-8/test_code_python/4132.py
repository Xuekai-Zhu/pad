def solution():
    # Define the growth rate for each year
    growth_rates = [2, 1.5, 1.5*1.5, 1.5*1.5*2, 1.5*1.5*2*0.5]

    # Calculate the height of the tree in each year
    heights = [2]
    for i in range(1, 5):
        height = heights[i-1] + growth_rates[i]
        heights.append(height)

    # Return the height of the tree in year 5
    result = heights[4]
    return result

print(solution())