def solution():
    initial_votes = 30
    remaining_students = 30
    surveyed_students = 5
    after_survey_students = 4
    total_possible_votes = 60
    needed_votes = total_possible_votes * 0.75 - initial_votes
    result = needed_votes
    return result

print(solution())