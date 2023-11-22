def solution():
    
    # Define the number of photographs that Jamal's phone can hold
    jamal_phone_capacity = 1800

    # Calculate the number of photographs that Brittany's phone can hold
    brittany_phone_capacity = jamal_phone_capacity / 6

    # Calculate the maximum number of photographs that Brittany's phone can hold
    brittany_max_capacity = brittany_phone_capacity * 50

    # Calculate the maximum number of ducks that can be seen in Jamal's phone
    jamal_max_capacity = jamal_phone_capacity - brittany_max_capacity

    # Display the maximum number of ducks that can be seen in Jamal's phone
    result = jamal_max_capacity
    return result

print(solution())