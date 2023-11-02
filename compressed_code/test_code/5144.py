def solution():
    
    first_store = 7
    second_store = first_store + 2
    third_store = 0
    fourth_store = 2 * (first_store + second_store + third_store)
    total_tries = first_store + second_store + third_store + fourth_store
    result = total_tries
    return result

print(solution())