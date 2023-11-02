def solution():
    initial_number = 3  # Molly plus her parents, who were there in the beginning
    additional_people = 100  # 100 people joined them during the day
    people_leaving = 40  # 40 people left at 5:00

    # Calculate the total number of people at the beach
    total_people = initial_number + additional_people - people_leaving
    result = total_people
    return result

print(solution())