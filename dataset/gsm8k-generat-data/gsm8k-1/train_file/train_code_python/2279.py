def solution():
    """Orlan gave one-fourth of his 20-meter rope to Allan. He then gave two-thirds of the remaining to Jack. How many meters of rope is left to Orlan?"""
    initial_rope = 20
    allan_rope = initial_rope / 4
    remaining_rope = initial_rope - allan_rope
    jack_rope = (2 / 3) * remaining_rope
    orlan_rope = remaining_rope - jack_rope
    result = orlan_rope
    return result

print(solution())