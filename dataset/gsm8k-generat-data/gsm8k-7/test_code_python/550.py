def solution():
    randy_initial = 3000
    smith_donation = 200
    sally_payment = 1200

    # Calculate Randy's total amount after Smith's donation
    randy_total = randy_initial + smith_donation

    # Calculate the amount Randy kept after giving Sally $1,200
    randy_kept = randy_total - sally_payment

    result = randy_kept
    return result

print(solution())