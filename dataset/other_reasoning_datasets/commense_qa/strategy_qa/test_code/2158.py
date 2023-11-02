def solution():
    sonnet_line_count = 14
    rime_line_count = 30
    if rime_line_count == sonnet_line_count:
        result = "maybe, but it would need significant editing"
    else:
        result = "no, it has too many lines"
    return result

print(solution())