def solution():
    """Benny saw a 10-foot shark with 2 6-inch remoras attached to it. What percentage of the shark's body length is the combined length of the remoras?"""
    shark_length_inches = 120
    remora_length_inches = 2 * 6
    combined_length_inches = shark_length_inches + remora_length_inches
    percentage_of_length = (combined_length_inches / shark_length_inches) * 100
    result = percentage_of_length
    return result

print(solution())