def solution():
    """June is running for class president. She needs just over 50% of the vote to win. There are 200 students in the school. 60% of students are boys and the rest are girls. If she receives 67.5% of male vote, what is the smallest percentage of the female she must receive to win the election?"""
    total_students = 200
    boys_percent = 60
    girls_percent = 100 - boys_percent
    boys_votes = total_students * (boys_percent / 100)
    girls_votes = total_students - boys_votes
    needed_votes = (total_students / 2) + 1
    votes_from_boys = boys_votes * 0.675
    votes_needed_from_girls = needed_votes - votes_from_boys
    girls_needed_percent = votes_needed_from_girls / girls_votes * 100
    result = girls_needed_percent
    return result

print(solution())