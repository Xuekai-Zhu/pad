def solution():
    # Find the number of capsules of 100 mg and 500 mg sold every week
    capsules_100mg = 80 / 5  # each capsule of 100 mg amoxicillin costs $5
    capsules_500mg = 60 / 2  # each capsule of 500 mg amoxicillin costs $2
    
    # Find the total number of capsules sold every 2 weeks
    capsules_sold = (capsules_100mg + capsules_500mg) * 2
    result = capsules_sold
    return result

print(solution())