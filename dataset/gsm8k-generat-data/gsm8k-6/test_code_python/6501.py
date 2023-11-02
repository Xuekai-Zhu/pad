def solution():
    # Calculate the number of clothes donated
    clothes_donated = 5 + (3*5)  # Amara donated 5 clothes to one orphanage home and triple that (5*3=15) to another orphanage home
    clothes_remaining = 100 - clothes_donated - 15  # Amara started with 100 clothes and threw away 15 and donated the others.
    result = clothes_remaining
    return result

print(solution())