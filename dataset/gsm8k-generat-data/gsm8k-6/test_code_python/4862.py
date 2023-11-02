def solution():
    # Calculate the number of correct items that Liza got
    correct_items_liza = 0.9 * 60  

    # Calculate the number of correct items that Rose got
    correct_items_rose = correct_items_liza + 2  

    # Calculate the number of incorrect items that Rose got
    incorrect_items_rose = 60 - correct_items_rose
    result = incorrect_items_rose
    return result

print(solution())