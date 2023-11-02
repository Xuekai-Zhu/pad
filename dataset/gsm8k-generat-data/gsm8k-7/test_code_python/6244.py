def solution():
    master_bed_bath = 500
    guest_bedrooms = 2 * 200
    kitchen_guestbath_living = 600
    total_sq_ft = master_bed_bath + guest_bedrooms + kitchen_guestbath_living
    monthly_rent = 3000
    cost_per_sq_ft = monthly_rent / total_sq_ft
    result = cost_per_sq_ft
    return result

print(solution())