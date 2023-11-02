def solution():
    
    total_students = 1000
    male_ratio = 3
    female_ratio = 2

    
    total_ratio = male_ratio + female_ratio
    num_male_students = int((male_ratio / total_ratio) * total_students)
    num_female_students = int((female_ratio / total_ratio) * total_students)

    
    num_male_basketball = int((2/3) * num_male_students)
    num_female_basketball = int((1/5) * num_female_students)

    
    num_not_basketball = total_students - num_male_basketball - num_female_basketball

    
    percent_not_basketball = (num_not_basketball / total_students) * 100

    result = percent_not_basketball
    return result

print(solution())