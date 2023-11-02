def solution():
    
    total_students = 400
    percent_invited = 70
    percent_revoked = 40
    
    invited_students = (percent_invited / 100) * total_students
    
    revoked_students = (percent_revoked / 100) * invited_students
    
    attending_students = invited_students - revoked_students
    
    result = attending_students
    
    return result

print(solution())