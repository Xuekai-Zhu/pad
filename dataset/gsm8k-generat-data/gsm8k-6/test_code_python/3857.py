def solution():
    # Calculate the number of times the quarterback does not throw a pass
    no_passes_thrown = 0.3 * 80

    # Calculate the number of times the quarterback is sacked for a loss
    sacked_for_loss = 0.5 * no_passes_thrown

    result = sacked_for_loss
    return result

print(solution())