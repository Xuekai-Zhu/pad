def solution():
    percent_increase = 25
    num_new_dolls = 2

    # Calculate the original number of dolls in Lucy's collection
    original_num_dolls = int((100 / (100 + percent_increase)) * (num_new_dolls))

    # Calculate the total number of dolls in Lucy's collection after the addition
    total_num_dolls = original_num_dolls + num_new_dolls
    result = total_num_dolls
    return result

print(solution())