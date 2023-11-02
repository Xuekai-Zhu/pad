def solution():
    """Beatrice is shopping for a new TV. First she looks at 8 TVs at one store in person. Then she looks at three times as many TVs at an online store. She looks at more TVs on an auction site online. If Beatrice looked at 42 TVs in all, how many did look at on the auction site?"""
    # Define the number of TVs Beatrice looks at in person
    tvs_in_person = 8

    # Calculate the number of TVs Beatrice looks at on the online store
    tvs_online = tvs_in_person * 3

    # Calculate the number of TVs Beatrice looks at on the auction site
    tvs_auction = 42 - tvs_in_person - tvs_online

    # Display the number of TVs Beatrice looks at on the auction site
    result = tvs_auction
    return result

print(solution())