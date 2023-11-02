def solution():
    # Define the minimum passing score and Jimmy's total points
    passing_score = 50
    total_points = 20 * 3 - 5

    # Calculate the points Jimmy can still lose and pass
    remaining_points = passing_score - total_points
    result = remaining_points
    return result

print(solution())