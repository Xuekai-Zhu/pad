def solution():
    percent_women = 0.5
    percent_men = 0.5
    percent_women_in_favor = 0.35
    num_women_opposed = 39

    # Calculate the total number of women who participated in the poll
    total_women = num_women_opposed / (1 - percent_women_in_favor)

    # Calculate the total number of people in the poll
    total_people = total_women / percent_women
    result = total_people
    return result

print(solution())