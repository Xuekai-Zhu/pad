def solution():
    num_mitten_pairs = 150

    # Calculate the number of plug pairs based on the number of mitten pairs
    num_plug_pairs = num_mitten_pairs + 20

    # Add 30 more pairs of plugs to the box
    num_plug_pairs += 30

    result = num_plug_pairs
    return result

print(solution())