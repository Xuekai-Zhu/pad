def solution():
    
    total_students = 40
    glasses_wearers = int(total_students * 0.25)
    contacts_wearers = int(total_students * 0.4)
    neither_wearers = total_students - glasses_wearers - contacts_wearers
    result = neither_wearers
    return result

print(solution())