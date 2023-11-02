def solution():
    # Calculate the total number of meat pieces used
    pepperoni = 30
    ham = 2 * pepperoni  # twice as many pieces of ham as pepperoni
    sausage = pepperoni + 12  # 12 more pieces of sausage than pepperoni
    total_meat = pepperoni + ham + sausage

    # Calculate the number of meat pieces on each slice of pizza
    slices = 6
    meat_per_slice = total_meat / slices
    result = meat_per_slice
    return result

print(solution())