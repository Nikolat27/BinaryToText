def binary_to_text(binary_string):
    binary_list = binary_string.split(" ")

    # Binary to Decimal conversion ( We do it for each binary value individually
    text = []
    for binary in binary_list:
        decimal_values = 0
        length = len(binary)
        for index in range(length):
            current_bit = binary[length - 1 - index]  # ( Right to left starting )
            if int(current_bit) != 0:
                decimal_values += (2 ** index)
        text.append(chr(decimal_values))

    return "".join(text)


x = binary_to_text("01110011 01100001 01101101")
print(x)
