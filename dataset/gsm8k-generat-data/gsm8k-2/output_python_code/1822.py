def solution():
    """Gerald thought it would be funny to trick his coworker, who's allergic to peanuts, into eating a peanut butter cookie. When his coworker goes into anaphylactic shock and is taken to the hospital, Gerald is arrested. The judge sentences Gerald to 3 months for assault and 2 years for poisoning, then extends his sentence by 1/3 since this is Gerald's third offense. How many months does Gerald spend in jail?"""
    assault_sentence = 3
    poisoning_sentence = 24
    total_sentence = assault_sentence + poisoning_sentence
    extended_sentence = total_sentence + (total_sentence / 3)
    months_in_jail = extended_sentence * 12
    result = months_in_jail
    return result

print(solution())