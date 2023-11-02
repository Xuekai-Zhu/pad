def solution():
    """June is running for class president.  She needs just over 50% of the vote to win.  There are 200 students in the school.  60% of students are boys and the rest are girls.  If she receives 67.5% of male vote, what is the smallest percentage of the female she must receive to win the election?"""
    # Define the number of students in the school and the percentage of boys
    total_students = 200
    boys_percentage = 0.6

    # Calculate the number of boys and girls
    boys = total_students * boys_percentage
    girls = total_students * (1 - boys_percentage)

    # Calculate the number of votes June needs to win
    votes_needed = (total_students // 2) + 1

    # Calculate the number of votes June has from boys
    boy_votes = boys * 0.675

    # Calculate the minimum percentage of votes June needs from girls to win
    girl_votes_needed = votes_needed - boy_votes
    girl_percentage_needed = (girl_votes_needed / girls) * 100

    # Return the result
    result = girl_percentage_needed
    return result

print(solution())