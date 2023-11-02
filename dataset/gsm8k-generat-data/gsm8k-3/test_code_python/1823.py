def solution():
    """Gerald thought it would be funny to trick his coworker, who's allergic to peanuts, into eating a peanut butter cookie. When his coworker goes into anaphylactic shock and is taken to the hospital, Gerald is arrested. The judge sentences Gerald to 3 months for assault and 2 years for poisoning, then extends his sentence by 1/3 since this is Gerald's third offense. How many months does Gerald spend in jail?"""
    # Define the original sentence lengths in months
    ASSAULT_SENTENCE = 3
    POISONING_SENTENCE = 24

    # Calculate the extended sentence length
    total_sentence = ASSAULT_SENTENCE + POISONING_SENTENCE
    extended_sentence = total_sentence * (1 + 1/3)

    # Convert the sentence length to months and round to the nearest month
    months_in_jail = round(extended_sentence * 12)

    # Display the number of months in jail
    result = months_in_jail
    return result

print(solution())