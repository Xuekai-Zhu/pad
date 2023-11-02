def solution():
    # Initial number of people and snack eaters
    total_people = 200
    snack_eaters = 100

    # 20 new outsiders joined in and had snacks
    snack_eaters += 20

    # Half of the snack eaters got full and left
    snack_eaters //= 2

    # 10 new outsiders joined in and had snacks
    snack_eaters += 10

    # 30 snack eaters got full and left
    snack_eaters -= 30

    # Half of the remaining snack eaters left
    snack_eaters //= 2

    result = snack_eaters
    return result

print(solution())