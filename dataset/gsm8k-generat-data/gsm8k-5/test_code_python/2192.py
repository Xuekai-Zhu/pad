def solution():
    total_distance = 5  # Suzanne is running a 5-kilometer race
    donation_per_kilometer = 10  # Suzanne's parents will donate $10 for her first kilometer
    total_donation = 0

    # Calculate the total donation based on the distance run
    for i in range(1, total_distance+1):
        if i == 1:
            total_donation += donation_per_kilometer
        else:
            donation_per_kilometer *= 2
            total_donation += donation_per_kilometer

    result = total_donation
    return result

print(solution())