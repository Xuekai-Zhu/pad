def solution():
    glucose_compound = "starch"
    wheelbarrow_capacity = 1200
    lethal_glucose_level = 0
    # Find out the amount of glucose in a wheelbarrow full of starch
    glucose_amount = glucose_compound.count("glucose") * wheelbarrow_capacity
    # Check if the glucose amount in the wheelbarrow exceeds the lethal glucose level
    if glucose_amount > lethal_glucose_level:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())