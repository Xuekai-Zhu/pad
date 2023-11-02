def solution():
    mikes_fruits = 3  # Mike received 3 oranges
    matts_fruits = 2 * mikes_fruits  # Matt got twice as many apples as Mike
    total_fruits = mikes_fruits + matts_fruits  # Total fruits received by Mike and Matt
    marks_fruits = total_fruits  # Mark got as many bananas as Mike and Matt received altogether

    # Calculate the total number of fruits Annie gave to her children
    total_children_fruits = mikes_fruits + matts_fruits + marks_fruits
    result = total_children_fruits
    return result

print(solution())