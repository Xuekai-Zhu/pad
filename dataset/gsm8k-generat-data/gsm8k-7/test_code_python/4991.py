def solution():
    total_students = 200
    percent_boys = 0.6
    percent_girls = 1 - percent_boys
    percent_vote_needed = 0.51
    percent_male_vote_received = 0.675

    # Calculate the total number of male and female students
    num_boys = total_students * percent_boys
    num_girls = total_students * percent_girls

    # Calculate the number of male votes June received
    num_male_votes = num_boys * percent_male_vote_received

    # Calculate the number of total votes needed to win
    num_votes_needed = total_students * percent_vote_needed

    # Calculate the number of female votes needed to win
    num_female_votes_needed = num_votes_needed - num_male_votes

    # Calculate the percentage of female votes needed to win
    percent_female_vote_needed = num_female_votes_needed / num_girls
    result = percent_female_vote_needed
    return result

print(solution())