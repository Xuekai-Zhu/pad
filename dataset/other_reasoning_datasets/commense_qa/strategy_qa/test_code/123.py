def solution():
    lupita_citizen_of_origin_country = False
    lupita_citizenships = ["Kenya", "Mexico"]
    obama_father_origin_country = "Kenya"
    obama_father_tribe = "Luo"
    
    if obama_father_origin_country in lupita_citizenships:
        lupita_citizen_of_origin_country = True
        
    result = "yes" if lupita_citizen_of_origin_country else "no"
    return result

print(solution())