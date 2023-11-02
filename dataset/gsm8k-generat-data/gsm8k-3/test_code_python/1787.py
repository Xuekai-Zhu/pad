def solution():
    """Kira is making breakfast for herself. She fries 3 sausages then scrambles 6 eggs and cooks each item of food separately. If it takes 5 minutes to fry each sausage and 4 minutes to scramble each egg then how long, in minutes, did it take for Kira to make her breakfast?"""
    # Define the time it takes to cook each item
    SAUSAGE_TIME = 5
    EGG_TIME = 4

    # Define the number of each item being cooked
    sausages = 3
    eggs = 6

    # Calculate the total cooking time
    total_time = (sausages * SAUSAGE_TIME) + (eggs * EGG_TIME)

    # Display the total cooking time
    result = total_time
    return result

print(solution())