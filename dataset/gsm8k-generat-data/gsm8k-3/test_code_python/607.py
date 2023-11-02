def solution():
    """Sandy bought 1 million Safe Moon tokens. She has 4 siblings. She wants to keep half of them to herself and divide the remaining tokens among her siblings. After splitting it up, how many more tokens will she have than any of her siblings?"""
    # Define the number of Safe Moon tokens Sandy bought
    tokens = 1000000

    # Calculate how many tokens Sandy keeps for herself
    sandy_tokens = tokens / 2

    # Calculate how many tokens each of Sandy's siblings gets
    sibling_tokens = (tokens - sandy_tokens) / 4

    # Calculate how many more tokens Sandy has than any of her siblings
    difference = sandy_tokens - sibling_tokens

    # Display the difference
    result = difference
    return result

print(solution())