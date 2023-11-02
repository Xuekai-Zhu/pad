def solution():
    augustus_rate = 3  # Augustus can make 3 milkshakes per hour
    luna_rate = 7  # Luna can make 7 milkshakes per hour
    hours_worked = 8  # Augustus and Luna have been making milkshakes for 8 hours

    # Calculate the total number of milkshakes they made
    total_milkshakes = (augustus_rate + luna_rate) * hours_worked
    result = total_milkshakes
    return result

print(solution())