def solution():
    """James runs a TV show and there are 5 main characters and 4 minor characters. He pays the minor characters $15,000 each episode. He paid the major characters three times as much. How much does he pay per episode?"""
    main_characters = 5
    minor_characters = 4
    minor_pay = 15000
    major_pay = minor_pay * 3
    total_pay = (main_characters * major_pay) + (minor_characters * minor_pay)
    result = total_pay
    return result

print(solution())