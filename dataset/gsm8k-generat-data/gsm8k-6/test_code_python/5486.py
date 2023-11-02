def solution():
    # Calculate the number of people attending the meeting
    num_attending = 300 / 2  # Half of all people will attend

    # Calculate the number of males and females attending the meeting
    num_males = 2/3 * num_attending  # Assume number of males is twice the number of females
    num_females = num_attending - num_males

    result = num_females
    return result

print(solution())