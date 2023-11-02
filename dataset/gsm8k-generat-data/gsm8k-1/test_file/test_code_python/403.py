Unfortunately, a solution for the Samantha's last name question is not provided. As for the Elliott's steps question, here's a solution:

def solution():
    """Elliott is trying to walk 10,000 steps a day. He finished half of his steps on his walks to and from school and did another 1,000 steps going for a short walk with his friend. He also went for a short jog around the block and realized that after he had finished his jog, he only had 2,000 steps left to take. How many steps did Elliott take during his jog?"""
    total_steps = 10000
    steps_to_and_from_school = total_steps / 2
    steps_with_friend = 1000
    remaining_steps = total_steps - (steps_to_and_from_school + steps_with_friend)
    steps_during_jog = remaining_steps - 2000
    result = steps_during_jog
    return result

print(solution())