def solution():
    # Calculate the total amount of fabric delivered on Monday and Tuesday
    fabric_monday = 20
    fabric_tuesday = 2 * fabric_monday

    # Calculate the amount of fabric delivered on Wednesday
    fabric_wednesday = fabric_tuesday / 4

    # Calculate the total amount of fabric delivered from Monday to Wednesday
    total_fabric = fabric_monday + fabric_tuesday + fabric_wednesday

    # Calculate the earnings from fabric sales
    fabric_earnings = total_fabric * 2

    # Calculate the earnings from yarn sales (assuming 0 yards of yarn were delivered)
    yarn_earnings = 0 * 3

    # Calculate the total earnings from Monday to Wednesday
    total_earnings = fabric_earnings + yarn_earnings
    result = total_earnings
    return result

print(solution())