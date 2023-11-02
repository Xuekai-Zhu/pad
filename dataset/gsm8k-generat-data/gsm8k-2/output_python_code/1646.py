def solution():
    """Ellie went to visit a circus with Sarah and they both got lost in the house of mirrors. They have to travel through the house of mirrors a few times before they finally get out and when they leave, they discuss how many times they've seen their own reflections. Sarah says that every time they were in the room with tall mirrors, she saw her reflection 10 times and every time they were in the room with wide mirrors, she saw her reflection 5 times. Ellie says that every time they were in the room with tall mirrors, she saw her reflection 6 times and every time they were in the room with wide mirrors she saw her reflection 3 times. They both passed through the room with tall mirrors 3 times each and they both passed through the room with wide mirrors 5 times each. In total, how many times did Sarah and Ellie see their reflections?"""
    sarah_tall_reflections = 10 * 3 * 2  # Sarah saw her reflection 10 times, passed through 3 times, and there are 2 tall mirrors rooms.
    sarah_wide_reflections = 5 * 5 * 2  # Sarah saw her reflection 5 times, passed through 5 times, and there are 2 wide mirrors rooms.
    ellie_tall_reflections = 6 * 3 * 2  # Ellie saw her reflection 6 times, passed through 3 times, and there are 2 tall mirrors rooms.
    ellie_wide_reflections = 3 * 5 * 2  # Ellie saw her reflection 3 times, passed through 5 times, and there are 2 wide mirrors rooms.
    total_reflections = sarah_tall_reflections + sarah_wide_reflections + ellie_tall_reflections + ellie_wide_reflections
    result = total_reflections
    return result

print(solution())