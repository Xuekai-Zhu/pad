def solution():
    total_students = 400
    freshmen_sophomores = total_students / 2
    freshmen_sophomores_with_pets = freshmen_sophomores / 5
    freshmen_sophomores_without_pets = freshmen_sophomores - freshmen_sophomores_with_pets
    result = freshmen_sophomores_without_pets
    return result

print(solution())