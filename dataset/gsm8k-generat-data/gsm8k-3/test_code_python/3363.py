def solution():
    """Joseph had socks of many different colors. His dresser drawer was filled to overflowing with red, blue, black, and white socks. Uncertain of how many pairs he had of each color, he began to sort his socks. He discovered that he had three more pairs of blue socks than he had pairs of black socks.  He had one less pair of red socks than he had pairs of white socks. He had twice as many blue socks as he had of red socks. And he counted a total of 6 red socks.  What is the total number of Joseph's socks?"""
    # Define the number of red socks
    red_socks = 6

    # Calculate the number of blue socks
    blue_socks = 2 * red_socks

    # Calculate the number of black socks
    black_socks = blue_socks - 3

    # Calculate the number of white socks
    white_socks = red_socks + 1

    # Calculate the total number of socks
    total_socks = 2 * (red_socks + blue_socks + black_socks + white_socks)

    # Display the total number of socks
    result = total_socks
    return result

print(solution())