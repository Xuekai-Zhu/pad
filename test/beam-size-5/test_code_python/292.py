def solution():
    rice_per_person = 0.2  # Each person consumes 0.2 kg of rice every meal
    num_people = 5  # There are 5 members in the household
    total_rice_per_person = rice_per_person * num_people  # Calculate the total amount of rice eaten per person
    total_rice_per_week = total_rice_per_person * 7  # Calculate the total amount of rice eaten per week
    weeks_of_rice = 42 / total_rice_per_week  # Calculate the number of weeks the bag of rice will last
    result = weeks_of_rice
    return result

print(solution())