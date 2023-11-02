def solution():
    jane_austen_birth_order = 2
    number_of_siblings = 8
    if jane_austen_birth_order == (number_of_siblings / 2):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())