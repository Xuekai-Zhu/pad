def solution():
    total_students = 300
    percent_females = 2/3
    percent_males = 1 - percent_females
    percent_foreign_males = 1/10
    percent_non_foreign_males = 1 - percent_foreign_males
    num_females = percent_females * total_students
    num_males = percent_males * total_students
    num_foreign_males = percent_foreign_males * num_males
    num_non_foreign_males = percent_non_foreign_males * num_males
    result = num_non_foreign_males
    
    return result

print(solution())