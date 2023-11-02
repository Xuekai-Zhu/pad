def solution():
    num_friends = 4  # Jessie invited 4 friends over to play
    total_muffins = 20  # They made 20 muffins in total

    # Calculate how many muffins each person will get
    muffins_per_person = total_muffins // (num_friends + 1)

    result = muffins_per_person
    return result

print(solution())