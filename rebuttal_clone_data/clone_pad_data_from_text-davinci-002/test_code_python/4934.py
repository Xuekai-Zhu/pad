def solution():
 
    Emma_ROI = 0.15
    Briana_ROI = 0.10
    Emma_capital = 300
    Briana_capital = 500
    years = 2
 
    Emma_total_ROI = Emma_capital + (Emma_capital * Emma_ROI * years)
    Briana_total_ROI = Briana_capital + (Briana_capital * Briana_ROI * years)
    difference = Emma_total_ROI - Briana_total_ROI
 
    return result

print(solution())