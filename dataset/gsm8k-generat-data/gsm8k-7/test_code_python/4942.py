def solution():
    total_points = 311
    combined_points = 188

    # Calculate the points scored by Lisa, Jessie, and Devin combined
    ljd_points = total_points - combined_points

    # Divide the points equally among Lisa, Jessie, and Devin
    jessie_points = ljd_points / 3
    result = jessie_points
    return result

print(solution())