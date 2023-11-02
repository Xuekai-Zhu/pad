def solution():
    
    hamburgers = 5 * 3
    french_fries = 4 * 1.2
    soda = 5 * 0.5
    spaghetti = 2.7
    total_bill = hamburgers + french_fries + soda + spaghetti
    bill_per_person = total_bill / 5
    result = bill_per_person
    return result

print(solution())