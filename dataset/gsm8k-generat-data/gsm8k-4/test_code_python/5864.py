def solution():
    """Before he lost one, Policeman O'Brien had 5 more than twice as many hats as fire chief Simpson. If fire chief Simpson has 15 hats, how many hats does Policeman O'Brien now have?"""
    # Define the number of hats owned by fire chief Simpson
    fire_chief_hats = 15

    # Calculate the number of hats owned by Policeman O'Brien before he lost one
    obrien_hats = 2 * fire_chief_hats + 5

    # Calculate the number of hats owned by Policeman O'Brien now
    obrien_hats_now = obrien_hats - 1

    # return the result
    result = obrien_hats_now
    return result

print(solution())