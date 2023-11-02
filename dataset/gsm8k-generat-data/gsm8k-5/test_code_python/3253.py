def solution():
    lions = 12
    tigers = 14
    cougars = (lions + tigers) / 2  # Cougars are half as many as lions and tigers combined
    total_big_cats = lions + tigers + cougars
    result = total_big_cats
    return result

print(solution())