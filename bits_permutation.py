def check_p_block(p_block, start_index):
    numbers = set(p_block)
    numbers_as_list = sorted(numbers)
    if sorted(p_block) == numbers_as_list:
        return True
    else:
        return False


def get_bit(data, bit_index, from_low_to_high):
    byte_index = bit_index // 8
    bit_in_byte = bit_index % 8
    if from_low_to_high:
        mask = 1 << bit_in_byte
    else:
        mask = 1 << (7 - bit_in_byte)

    return 1 if (data[byte_index] & mask) else 0


def set_bit(result, bit_index, value, from_low_to_high):
    byte_index = bit_index // 8
    bit_in_byte = bit_index % 8
    if from_low_to_high:
        mask = 1 << bit_in_byte
    else:
        mask = 1 << (7 - bit_in_byte)

    if value == 1:
        result[byte_index] |= mask
    else:
        result[byte_index] &= ~mask


def permute_bits(data, p_block, from_low_to_high, start_index):
    total_bits = len(data) * 8
    result = [0] * len(data)

    if total_bits != len(p_block):
        raise IndexError("P_block doesn't fit with data")

    if start_index not in (0, 1):
        raise ValueError("Incorrect start index")

    for i in range(total_bits):
        source_index = p_block[i] - start_index
        bit_value = get_bit(data, source_index, from_low_to_high)
        set_bit(result, i, bit_value, from_low_to_high)

    return result


def main():
    data = [0b10110010]
    p_block = [7, 6, 5, 4, 3, 2, 1, 0]
    from_low_to_high = True
    start_index = 0

    try:
        result = permute_bits(data, p_block, from_low_to_high, start_index)
    except IndexError as e:
        print(f"Error: {e}")
        return
    except ValueError as e:
        print(f"Error: {e}")
        return

    if check_p_block(p_block, start_index):
        print("P_block is filled")
    else:
        print("P_block is incorrect")

    print(f"Example data (1 byte): {data[0]}")
    print(f"Permuted data: {result[0]}")


if __name__ == "__main__":
    main()
