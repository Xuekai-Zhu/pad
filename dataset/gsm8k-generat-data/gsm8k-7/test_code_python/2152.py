def solution():
    num_jellybeans = 70
    num_nephews = 3
    num_nieces = 2

    # Calculate the total number of jellybeans each person will receive
    total_jellybeans_per_person = num_jellybeans / (num_nephews + num_nieces)

    result = total_jellybeans_per_person
    return result

print(solution())