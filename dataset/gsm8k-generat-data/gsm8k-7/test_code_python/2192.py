def solution():
    num_kilometers = 5
    first_kilometer_donation = 10

    total_donation = 0
    current_donation = first_kilometer_donation

    for i in range(num_kilometers):
        total_donation += current_donation
        current_donation *= 2

    result = total_donation
    return result

print(solution())