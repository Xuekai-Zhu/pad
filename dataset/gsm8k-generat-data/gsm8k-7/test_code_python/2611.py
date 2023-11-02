def solution():
    current_age_trevor = 11
    current_age_brother = 20

    # Set a variable to keep track of how much older the brother is than Trevor
    age_difference = current_age_brother - current_age_trevor

    # Set up a loop to find when the brother will be three times as old as Trevor
    while current_age_brother != current_age_trevor * 3:
        current_age_trevor += 1
        current_age_brother += 1
        age_difference += 1

    # When the loop exits, Trevor will be the same age as his brother was when he was three times Trevor's age
    # That age difference can be added to Trevor's current age to find the answer to the question
    result = current_age_trevor + age_difference
    return result

print(solution())