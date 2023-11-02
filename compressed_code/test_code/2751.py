def solution():
    
    days_late_book1 = 20
    days_late_books2and3 = 31 
    late_charges_book1 = 0.5 * days_late_book1
    late_charges_books2and3 = 0.5 * days_late_books2and3 * 2
    total_charges = late_charges_book1 + late_charges_books2and3
    result = total_charges
    return result

print(solution())