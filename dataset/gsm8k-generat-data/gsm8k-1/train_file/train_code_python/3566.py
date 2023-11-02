def solution():
    """On the night of the dance, 400 students show up to the party. 70% of the students who showed up were invited. If 40% of those invited to the party had their invitation revoked and were not allowed into the party, how many invited students attended the party?"""
    total_students = 400
    percent_invited = 70
    percent_revoked = 40
    
    invited_students = (percent_invited / 100) * total_students
    
    revoked_students = (percent_revoked / 100) * invited_students
    
    attending_students = invited_students - revoked_students
    
    result = attending_students
    
    return result

print(solution())