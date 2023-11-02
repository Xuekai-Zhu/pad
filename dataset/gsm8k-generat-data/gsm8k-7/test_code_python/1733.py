def solution():
    num_pants = 4
    num_jumpers = 4
    num_pajamas = 4
    num_tshirts = 20

    num_friends = 3
    total_donations = (num_pants + num_jumpers + num_pajamas + num_tshirts) * num_friends

    num_kept = (num_pants + num_jumpers + num_pajamas + num_tshirts) / 2

    num_donated = total_donations + num_kept
    result = num_donated
    return result

print(solution())