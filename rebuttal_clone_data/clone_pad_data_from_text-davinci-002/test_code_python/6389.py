def solution():
     original_trashcans_in_central_park = 8 + (24 / 2)
     original_trashcans_in_veterans_park = 24
     total_trashcans = original_trashcans_in_central_park + original_trashcans_in_veterans_park
     trashcans_removed_from_central_park = total_trashcans / 2
     trashcans_in_veterans_park = original_trashcans_in_veterans_park + trashcans_removed_from_central_park
     result = trashcans_in_veterans_park
 
     return result

print(solution())