def solution():
    current_cows = 200  # Rancher currently has 200 cows
    new_cows = current_cows / 2  # Number of new cows born each year is half the current number of cows
    total_cows = current_cows + new_cows  # Total number of cows after one year
    total_cows += (total_cows / 2)  # Number of new cows born in second year is half the total number of cows
    result = total_cows
    return result

print(solution())