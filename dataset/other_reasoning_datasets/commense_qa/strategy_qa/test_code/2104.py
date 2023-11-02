def solution():
    president_name = "Abdulqawi Yusuf"
    icj_headquarters = "The Hague"
    # Assume that the president typically works at the headquarters
    typical_work_location = icj_headquarters
    if typical_work_location == icj_headquarters:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())