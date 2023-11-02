def solution():
    # Calculate the number of male and female students based on the given ratio
    total_students = 1000
    male_students = (3/5) * total_students
    female_students = (2/5) * total_students

    # Calculate the number of students who do NOT like basketball based on the given proportions
    male_basketball_players = (2/3) * male_students
    female_basketball_players = (1/5) * female_students
    non_basketball_players = total_students - male_basketball_players - female_basketball_players

    # Calculate the percentage of the population that does not like basketball
    percent_non_basketball = (non_basketball_players / total_students) * 100
    result = percent_non_basketball
    return result

print(solution())