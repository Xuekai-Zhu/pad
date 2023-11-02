def solution():
    is_Iyer_caste = True
    is_Brahmin = True
    do_priests_not_eat_meat = True
    # Check if people of the Iyer caste eat meat
    if is_Iyer_caste and is_Brahmin and do_priests_not_eat_meat:
        result = "no"
    else:
        result = "uncertain"
    return result

print(solution())