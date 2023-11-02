def solution():
     letters_to_mail = 4
     international_letters = 2
     standard_postage = 1.08
     total_postage = 4.60
     international_postage_charge = total_postage - (standard_postage * letters_to_mail)
     charge_per_letter = international_postage_charge / international_letters
     result = charge_per_letter
     return result

print(solution())