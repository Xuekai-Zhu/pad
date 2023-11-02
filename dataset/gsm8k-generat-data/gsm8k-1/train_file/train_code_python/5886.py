def solution():
    """Nina has four times more math homework and eight times more reading homework than Ruby. If Ruby has six math and two reading homework, how much homework is Nina having altogether?"""
    ruby_math_hw = 6
    ruby_read_hw = 2
    nina_math_hw = 4 * ruby_math_hw
    nina_read_hw = 8 * ruby_read_hw
    total_hw = nina_math_hw + nina_read_hw + ruby_math_hw + ruby_read_hw
    result = total_hw
    return result

print(solution())