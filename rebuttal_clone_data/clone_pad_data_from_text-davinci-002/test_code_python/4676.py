def solution():
    max_donation = 1200
    half_donation = max_donation / 2
    total_donations = (max_donation * 500) + (half_donation * 1500)
    percent_total = 40
    total_raised = total_donations * (percent_total / 100)
    
    return total_raised

print(solution())