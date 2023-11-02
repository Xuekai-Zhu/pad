def solution():
    total_guests = 30  # Wickham invites 30 people
    plus_ones = total_guests // 2  # Half of the guests bring a plus one
    total_guests += plus_ones  # Add the plus ones to the total guest count
    total_courses = 3  # Wickham is serving a 3-course meal

    # Calculate the total number of plates needed for the guests
    total_plates = total_guests * total_courses
    result = total_plates
    return result

print(solution())