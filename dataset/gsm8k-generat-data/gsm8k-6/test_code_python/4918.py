def solution():
    # Calculate the number of points scored by Michiko
    michiko_points = 14 / 2  # Michiko scored half as many points as Bailey

    # Calculate the number of points scored by Akiko
    akiko_points = michiko_points + 4  # Akiko scored 4 more points than Michiko

    # Calculate the number of points scored by Chandra
    chandra_points = 2 * akiko_points  # Chandra scored twice as many points as Akiko

    # Calculate the total number of points scored by the team
    total_points = bailey_points + michiko_points + akiko_points + chandra_points

    result = total_points
    return result

print(solution())