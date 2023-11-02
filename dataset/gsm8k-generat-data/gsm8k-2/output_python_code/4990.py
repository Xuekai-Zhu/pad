def solution():
    """June is running for class president. She needs just over 50% of the vote to win. There are 200 students in the school. 60% of students are boys and the rest are girls. If she receives 67.5% of male vote, what is the smallest percentage of the female she must receive to win the election?"""
    total_students = 200
    boys_percent = 60
    girls_percent = 100 - boys_percent
    boys_count = total_students * (boys_percent / 100)
    girls_count = total_students - boys_count
    vote_needed = total_students / 2 + 1
    male_vote = boys_count * (67.5 / 100)
    remaining_vote_needed = vote_needed - male_vote
    female_vote_needed = remaining_vote_needed / girls_count
    result = round(female_vote_needed * 100, 2)
    return result

print(solution())