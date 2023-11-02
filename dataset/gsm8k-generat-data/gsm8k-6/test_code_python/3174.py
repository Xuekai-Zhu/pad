def solution():
    # Calculate the total number of people who attended the party
    total_people = 30 + 20  

    # Calculate the number of people who left the party
    left_people = (2/5) * total_people

    # Calculate the number of women who stayed at the party
    women_left = total_people - left_people - 20  # women left = total_people - left_people - men_left

    # Calculate the number of men who stayed at the party
    men_left = 20 - 9  

    # Calculate the difference between the number of women and men who stayed
    diff = women_left - men_left
    result = diff
    return result

print(solution())