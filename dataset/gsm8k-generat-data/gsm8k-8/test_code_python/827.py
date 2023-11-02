def solution():
    # Define the number of chairs in each row and rows in the church
    chairs_per_row = 6
    rows_in_church = 20

    # Calculate the total number of chairs in the church
    total_chairs = chairs_per_row * rows_in_church

    # Calculate the number of people that can sit in each chair
    people_per_chair = 5

    # Calculate the total number of people that can sit in all the chairs
    total_people = total_chairs * people_per_chair
    result = total_people
    return result

print(solution())