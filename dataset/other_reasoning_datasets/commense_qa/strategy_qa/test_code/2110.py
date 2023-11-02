def solution():
    # Define J. P. Morgan's smoking habits (assuming he smoked during his lifetime)
    cigars_per_day = "dozens"
    smoking_damages_lungs = True
    # Check if his smoking habit would affect his lung health
    if cigars_per_day != "none" and smoking_damages_lungs:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())