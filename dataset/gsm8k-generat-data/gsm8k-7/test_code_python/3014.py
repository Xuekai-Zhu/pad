def solution():
    num_bowls = 638
    safe_bowl_fee = 3  # fee for every bowl that is safely delivered
    lost_bowl_fee = 4  # fee for every bowl that is lost or broken
    lost_bowls = 12
    broken_bowls = 15

    # Calculate the total fee for safely delivering all bowls
    safe_bowl_total_fee = safe_bowl_fee * (num_bowls - lost_bowls - broken_bowls)

    # Calculate the total fee for lost/broken bowls
    lost_bowl_total_fee = lost_bowl_fee * (lost_bowls + broken_bowls)

    # Calculate the total payment that Travis should receive
    total_payment = safe_bowl_total_fee - lost_bowl_total_fee + 100
    result = total_payment
    return result

print(solution())