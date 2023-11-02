def solution():
    # Define the length of rope Bob has and the length he used for his art
    total_rope = 50
    art_rope = total_rope / 5

    # Calculate the length of rope Bob has left
    remaining_rope = total_rope - art_rope

    # Calculate the length of rope Bob gives to his friend
    friend_rope = remaining_rope / 2

    # Calculate the number of 2-foot sections Bob can cut from the remaining rope
    sections = friend_rope // 2

    result = sections
    return result

print(solution())