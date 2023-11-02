def solution():
    
    rent = 1200
    mrs_mcpherson_contribution = 0.3 * rent
    mr_mcpherson_contribution = rent - mrs_mcpherson_contribution
    result = mr_mcpherson_contribution
    return result

print(solution())