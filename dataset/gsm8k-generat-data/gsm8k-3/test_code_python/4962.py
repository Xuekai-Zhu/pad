def solution():
    """Kendra wants enough shirts that she only has to do laundry once every two weeks. She wears one shirt to school for each of the five weekdays. Three days a week, she changes into a different shirt for an after-school club. On Saturday, she wears one shirt all day. On Sunday, she wears a different shirt to church than she does for the rest of the day. How many shirts does she need to be able to only do laundry once every two weeks?"""
    # Calculate the number of shirts Kendra wears in a week
    daily_shirts = 5 + 3 + 1 + 2 # 5 for school, 3 for after-school club, 1 for Saturday, 2 for Sunday
    weekly_shirts = daily_shirts * 7

    # Calculate the number of shirts Kendra needs for two weeks
    total_shirts = weekly_shirts * 2

    # Display the total number of shirts needed
    result = total_shirts
    return result

print(solution())