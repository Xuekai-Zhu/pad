def solution():
    """Kendra wants enough shirts that she only has to do laundry once every two weeks. She wears one shirt to school for each of the five weekdays. Three days a week, she changes into a different shirt for an after-school club. On Saturday, she wears one shirt all day. On Sunday, she wears a different shirt to church than she does for the rest of the day. How many shirts does she need to be able to only do laundry once every two weeks?"""
    weekdays = 5
    after_school_days = 3
    weekend_days = 2
    total_shirts_needed = (weekdays + after_school_days + weekend_days) * 2
    result = total_shirts_needed
    return result

print(solution())