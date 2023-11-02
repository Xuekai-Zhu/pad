def solution():
    """June is running for class president.  She needs just over 50% of the vote to win.  There are 200 students in the school.  60% of students are boys and the rest are girls.  If she receives 67.5% of male vote, what is the smallest percentage of the female she must receive to win the election?"""
    # Calculate the number of boys and girls in the school
    num_boys = 0.6 * 200
    num_girls = 0.4 * 200

    # Calculate the number of votes needed to win
    votes_needed = 0.5 * 200 + 1

    # Calculate the number of votes June already has from the boys
    votes_from_boys = 0.675 * num_boys

    # Calculate the minimum percentage of the girls' vote June needs to win
    votes_needed_from_girls = votes_needed - votes_from_boys
    percentage_needed_from_girls = (votes_needed_from_girls / num_girls) * 100

    # Display the minimum percentage needed from the girls' vote
    result = percentage_needed_from_girls
    return result

print(solution())