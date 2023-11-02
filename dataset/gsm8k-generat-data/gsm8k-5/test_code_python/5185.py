def solution():
    # Calculate the number of swordfish caught by Shelly in each fishing trip
    shelly_catch = []
    for i in range(5):
        num_swordfish = (5 - 2) - 2*i
        shelly_catch.append(num_swordfish)

    # Calculate the number of swordfish caught by Sam in each fishing trip
    sam_catch = []
    for fish in shelly_catch:
        sam_catch.append(fish - 1)

    # Calculate the total number of swordfish caught by both of them in 5 trips
    total_catch = sum(shelly_catch) + sum(sam_catch)
    result = total_catch
    return result

print(solution())