def solution():
    is_bengal_carnivore = True
    pancakes_contain_meat = False
    if is_bengal_carnivore and not pancakes_contain_meat:
        result = "no" # Bengal cats cannot survive on pancakes alone
    else:
        result = "yes"
    return result

print(solution())