def solution():
    total_students = 200  # There are 200 students in the school
    boys_percentage = 60  # 60% of students are boys
    girls_percentage = 100 - boys_percentage  # The rest are girls
    required_percentage = 50.1  # June needs just over 50% of the vote to win

    # Calculate the number of boys and girls in the school
    num_boys = total_students * (boys_percentage / 100)
    num_girls = total_students - num_boys

    # Calculate the number of votes June needs to win
    required_votes = total_students * (required_percentage / 100)

    # Calculate the number of votes June has already received from boys
    boys_vote_percentage = 67.5  # June has received 67.5% of the male vote
    boys_votes = num_boys * (boys_vote_percentage / 100)

    # Calculate the smallest percentage of the female vote June needs to win
    required_female_vote = (required_votes - boys_votes) / num_girls
    result = required_female_vote * 100
    return result

print(solution())