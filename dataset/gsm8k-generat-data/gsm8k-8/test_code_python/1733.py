def solution():
    # Calculate the initial number of clothes
    initial_clothes = 4 + 4 + 4 * 2 + 20

    # Calculate the number of clothes Adam keeps
    clothes_kept = initial_clothes / 2

    # Calculate the number of clothes donated by Adam
    clothes_donated_by_adam = initial_clothes - clothes_kept

    # Calculate the number of clothes donated by each friend
    clothes_donated_by_friend = clothes_donated_by_adam / 3

    # Calculate the total number of clothes donated
    total_clothes_donated = clothes_donated_by_adam + clothes_donated_by_friend * 3
    result = total_clothes_donated
    return result

print(solution())