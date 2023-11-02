def solution():
    """Joseph had socks of many different colors. His dresser drawer was filled to overflowing with red, blue, black, and white socks. Uncertain of how many pairs he had of each color, he began to sort his socks. He discovered that he had three more pairs of blue socks than he had pairs of black socks.
    He had one less pair of red socks than he had pairs of white socks. He had twice as many blue socks as he had of red socks. And he counted a total of 6 red socks. What is the total number of Joseph's socks?"""
    # Define the number of blue socks in terms of red socks
    blue_socks = 2 * 6

    # Define the number of black socks in terms of blue socks
    black_socks = blue_socks - 3

    # Define the number of white socks in terms of red socks
    white_socks = 6 + 1

    # Calculate the total number of pairs of socks
    total_pairs = (6 // 2) + (blue_socks // 2) + (black_socks // 2) + (white_socks // 2)

    # Calculate the total number of socks
    total_socks = total_pairs * 2

    # Return the result
    result = total_socks
    return result

print(solution())