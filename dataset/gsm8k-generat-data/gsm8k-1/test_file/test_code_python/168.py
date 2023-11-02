def solution():
    """There are four birds at the Caboose. Sally Two is three years older than Granny Red. Granny Red is two times as old as Sally Four. If Sally Four is the same age as Sally Thirtytwo, and Sally Thirtytwo is 8 years old, what's the total age of the four birds?"""
    sally_thirtytwo_age = 8
    sally_four_age = sally_thirtytwo_age
    granny_red_age = sally_four_age * 2
    sally_two_age = granny_red_age + 3
    total_age = sally_two_age + granny_red_age + sally_four_age + sally_thirtytwo_age
    result = total_age
    return result

print(solution())