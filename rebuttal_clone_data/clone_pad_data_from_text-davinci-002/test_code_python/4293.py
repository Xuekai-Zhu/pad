def solution():
    total_cds = 200
    cds_at_ten = total_cds * 0.4
    cds_at_five = total_cds - cds_at_ten
    prince_spent = cds_at_five * 5 + cds_at_ten * 10
    result = prince_spent
    return result

print(solution())