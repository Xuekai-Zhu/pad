def solution():
    # Calculate the percentage of women in favor of shortening the school day
    women_in_favor = 35/100

    # Calculate the number of women in the poll
    women = 39 / (1 - women_in_favor)

    # Calculate the total number of people in the poll
    total_people = women * 2  # making sure to get answers from 50% men and 50% women
    result = total_people
    return result

print(solution())