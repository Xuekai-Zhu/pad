def solution():
    
    num_employees = 5
    rudy_wpm = 64
    joyce_wpm = 76
    gladys_wpm = 91
    lisa_wpm = 80
    mike_wpm = 89
    total_wpm = rudy_wpm + joyce_wpm + gladys_wpm + lisa_wpm + mike_wpm
    avg_wpm = total_wpm / num_employees
    result = avg_wpm
    return result

print(solution())