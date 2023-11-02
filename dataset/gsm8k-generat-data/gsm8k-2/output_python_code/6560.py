def solution():
    """Bob buys 50 feet of rope. He uses a 5th of it to make a small piece of art. He takes the rest and gives half of it to the friend. After that, he cuts 2-foot sections. How many sections does he get?"""
    total_rope = 50
    art_rope = total_rope / 5
    remaining_rope = total_rope - art_rope
    friend_rope = remaining_rope / 2
    cutting_rope = friend_rope
    sections = cutting_rope / 2
    result = sections
    return result

print(solution())