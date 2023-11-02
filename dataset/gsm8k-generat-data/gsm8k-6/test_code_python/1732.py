def solution():
    # Calculate the total number of scoops of ice cream
    total_scoops = 10 * 3  # 3 cartons, each containing 10 scoops
    # Calculate the number of scoops taken
    scoops_taken = 1 + 1 + 2*3 + 1 + 2 + 2 + 2  # Ethan takes 1 scoop of vanilla and 1 scoop of chocolate, Luke, Danny, and Connor take 2 scoops of chocolate each, Olivia takes 1 scoop of vanilla and 1 scoop of strawberry, Shannon takes twice as much as Olivia
    # Subtract the scoops taken from the total
    scoops_left = total_scoops - scoops_taken
    result = scoops_left
    return result

print(solution())