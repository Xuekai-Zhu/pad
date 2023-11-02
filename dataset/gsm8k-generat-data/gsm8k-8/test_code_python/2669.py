def solution():
    # Define the number of TVs Beatrice looked at in the first store
    in_person = 8

    # Define the number of TVs Beatrice looked at on the online store
    online = 3 * in_person

    # Calculate the number of TVs Beatrice looked at on the auction site
    auction = 42 - in_person - online

    result = auction
    return result

print(solution())