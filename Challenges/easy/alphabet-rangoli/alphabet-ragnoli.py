def rangoli(size):
    import string
    alphabet = string.ascii_lowercase

    lines = []
    # Construct each line of the pattern
    for i in range(size):
        # Build the line from end to middle
        left_part = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        line = left_part.center(4 * size - 3, '-')
        lines.append(line)

    # Form the full pattern by combining top and bottom parts
    pattern = '\n'.join(lines[::-1] + lines[1:])
    return pattern

# Example usage:
size = int(input().strip())
result = rangoli(size)
print(result)
