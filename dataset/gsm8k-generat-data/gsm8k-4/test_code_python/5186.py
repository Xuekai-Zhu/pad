def solution():
    """8 years ago James was twice Janet's age. In 15 years James will turn 37. Susan was born when Janet turned 3. How old will Susan turn in 5 years?"""
    # Let's define the present age of James as 'j' and Janet as 'jnt'
    # Present age of Susan will be 'jnt + 3 + 5'

    # Let's first find the present age of James
    j = 15 + 37 - 15  # James will turn 37 in 15 years, so his current age will be 37-15=22

    # Let's find Janet's present age
    jnt = (j - 8) / 2  # 8 years ago James was twice Janet's age, so j=2jnt+8 => jnt=(j-8)/2

    # Susan was born when Janet turned 3, so her current age will be jnt + 3 + 5
    susan_age = jnt + 3 + 5

    # In 5 years, Susan will be 5 years older
    susan_age_in_5_years = susan_age + 5

    result = susan_age_in_5_years
    return result

print(solution())