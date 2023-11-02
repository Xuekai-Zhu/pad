def solution():
    """Kira is making breakfast for herself. She fries 3 sausages then scrambles 6 eggs and cooks each item of food separately. If it takes 5 minutes to fry each sausage and 4 minutes to scramble each egg then how long, in minutes, did it take for Kira to make her breakfast?"""
    # Calculate the time it takes to fry the sausages
    sausage_time = 3 * 5

    # Calculate the time it takes to scramble the eggs
    egg_time = 6 * 4

    # Calculate the total time to make breakfast
    total_time = sausage_time + egg_time

    # return the result
    result = total_time
    return result

print(solution())