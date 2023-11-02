def solution():
    jellybeans_in_jar = 100  # There are 100 jellybeans in the jar
    students_present = 22  # 24 kids - 2 who stayed home sick
    jellybeans_eaten = students_present * 3  # Each student eats 3 jellybeans
    jellybeans_left = jellybeans_in_jar - jellybeans_eaten  # Calculate the number of jellybeans left in the jar
    result = jellybeans_left
    return result

print(solution())