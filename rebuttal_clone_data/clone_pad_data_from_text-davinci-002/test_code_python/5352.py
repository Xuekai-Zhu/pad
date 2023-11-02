def solution():
    total_age = 31
    dante_age = total_age - (2 * cooper_age) - maria_age
    maria_age = dante_age + 1
    cooper_age = (total_age - dante_age) / 2
    result = cooper_age
    return result

print(solution())