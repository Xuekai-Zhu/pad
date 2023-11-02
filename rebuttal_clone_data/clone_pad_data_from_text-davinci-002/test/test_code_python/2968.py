def solution():
    four_person_tables = 16
    six_person_tables = 4
    ten_person_tables = 8
    four_person_capacity = four_person_tables * 4
    six_person_capacity = six_person_tables * 6
    ten_person_capacity = ten_person_tables * 10
    total_capacity = four_person_capacity + six_person_capacity + ten_person_capacity
    result = total_capacity
    return result

print(solution())