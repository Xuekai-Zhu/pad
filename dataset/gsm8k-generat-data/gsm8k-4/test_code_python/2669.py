def solution():
    """Beatrice is shopping for a new TV. First she looks at 8 TVs at one store in person. Then she looks at three times as many TVs at an online store. She looks at more TVs on an auction site online. If Beatrice looked at 42 TVs in all, how many did look at on the auction site?"""
    # Define the number of TVs Beatrice looked at in person
    in_person = 8

    # Define the ratio of TVs looked at on the online store to those looked at in person
    online_ratio = 3

    # Calculate the total number of TVs looked at on the online store
    online = in_person * online_ratio

    # Calculate the number of TVs looked at on the auction site
    auction = 42 - in_person - online

    # return the result
    result = auction
    return result

print(solution())