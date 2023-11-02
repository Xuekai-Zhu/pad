def solution():
    # Calculate the total points for Joe's team
    joe_points = 3*1 + 1*3  # 1 win and 3 draws
    
    # Calculate the total points for the first-place team
    first_place_points = 3*2 + 1*2  # 2 wins and 2 draws
    
    # Calculate the difference in points between the two teams
    difference = first_place_points - joe_points
    result = difference
    return result

print(solution())