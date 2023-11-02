def solution():
    """Four adults with 32 teeth went to the dentist for a checkup after realizing they were having severe tooth pain. They were found to have different numbers of damaged teeth, and each person had some teeth removed. The first person had 1/4 of all his teeth removed, and the second person had 3/8 of his teeth removed, the third person had half of his teeth removed, while the last person only had 4 teeth removed. What's the total number of teeth removed at the dental clinic?"""
    total_teeth = 32
    person1_removed = total_teeth * (1/4)
    person2_removed = total_teeth * (3/8)
    person3_removed = total_teeth * (1/2)
    person4_removed = 4
    total_removed = person1_removed + person2_removed + person3_removed + person4_removed
    result = total_removed
    return result

print(solution())