def solution():
    rope1 = 8
    rope2 = 20
    rope3 = 2
    rope4 = 2
    rope5 = 2
    rope6 = 7
    total_rope = rope1 + rope2 + rope3 + rope4 + rope5 + rope6
    knots = 5
    knot_loss = 1.2
    total_loss = knots * knot_loss
    rope_length = total_rope - total_loss
    result = rope_length
    return result

print(solution())