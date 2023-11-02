def solution():
    # Calculate the total length needed to fence the field
    total_length = 4 * 5000

    # Calculate the cost of the wire mesh needed
    cost = total_length * 30

    # Calculate the length of fence that can be bought with the given budget
    length_purchased = cost // 30

    # Calculate the length of unfenced area
    unfenced_length = total_length - length_purchased

    result = unfenced_length
    return result

print(solution())