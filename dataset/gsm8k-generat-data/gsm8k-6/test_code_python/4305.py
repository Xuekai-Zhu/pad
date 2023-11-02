def solution():
    # Calculate the total number of crates sold by Gabrielle in 4 days
    monday_crates = 5
    tuesday_crates = 2 * monday_crates
    wednesday_crates = tuesday_crates - 2
    thursday_crates = tuesday_crates / 2
    total_crates = monday_crates + tuesday_crates + wednesday_crates + thursday_crates
    result = total_crates
    return result

print(solution())