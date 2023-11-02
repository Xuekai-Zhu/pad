def solution():
    feet_per_story = 10
    total_feet = feet_per_story * 6
    rope_length = 20
    percent_loss = 25
    length_lost = rope_length * (percent_loss / 100)
    usable_length = rope_length - length_lost
    pieces_of_rope = total_feet / usable_length
    return pieces_of_rope

print(solution())