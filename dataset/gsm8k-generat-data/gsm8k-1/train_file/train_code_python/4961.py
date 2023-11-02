def solution():
    """Kendra wants enough shirts that she only has to do laundry once every two weeks. She wears one shirt to school for
    each of the five weekdays. Three days a week, she changes into a different shirt for an after-school club. On Saturday,
    she wears one shirt all day. On Sunday, she wears a different shirt to church than she does for the rest of the day. 
    How many shirts does she need to be able to only do laundry once every two weeks?"""
    school_shirts = 5 * 2 # wear each shirt twice a week
    after_school_club_shirts = 3 * 2 # wear each shirt twice a week
    saturday_shirts = 1
    sunday_shirts = 2 # wear one shirt for church and one for the rest of the day
    total_shirts = school_shirts + after_school_club_shirts + saturday_shirts + sunday_shirts
    result = total_shirts
    return result

print(solution())