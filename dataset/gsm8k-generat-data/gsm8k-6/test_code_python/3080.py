def solution():
    # Calculate the number of fishes that Tony will have in 5 years
    fish_count = 2  # Tony starts with 2 fish
    for i in range(5):
        fish_count += 1  # Tony gets 2 more fish each year
        fish_count -= 1  # One fish dies each year
    result = fish_count
    return result

print(solution())