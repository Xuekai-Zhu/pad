def solution():
    adrenaline_production = "adrenal glands"
    tumor_formation = "tumors"
    tumor_location = "adrenal glands"
    if tumor_formation in cancer and tumor_location == adrenaline_production:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())