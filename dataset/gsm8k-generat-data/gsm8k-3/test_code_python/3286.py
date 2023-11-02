def solution():
    """John decides to get a new phone number and it ends up being a recycled number.  He used to get 20 text messages a day.  Now he is getting 55.  Assuming the number of texts his friends send has not changed, how many text messages per week is he getting that are not intended for him?"""
    # Calculate the extra texts per day
    extra_texts = 55 - 20

    # Calculate the extra texts per week
    extra_texts_week = extra_texts * 7

    # Display the extra texts per week
    result = extra_texts_week
    return result

print(solution())