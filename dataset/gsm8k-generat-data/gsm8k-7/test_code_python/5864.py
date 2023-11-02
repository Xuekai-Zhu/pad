def solution():
    # First, we need to find how many hats Policeman O'Brien had before.
    # We know he had 5 more than twice as many hats as fire chief Simpson, who has 15.
    obrien_hats = 5 + 2 * 15  # 35 hats

    # However, we also know that he lost one hat.
    obrien_hats -= 1

    result = obrien_hats
    return result

print(solution())