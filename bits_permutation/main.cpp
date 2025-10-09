#include <iostream>
#include "vector"
#include <cstdint>
#include "cmath"


uint8_t get_bit(std::vector<uint8_t> &data, int bit_index, bool from_low_to_high) {
    int byte_index = bit_index / 8;
    int bit_in_byte = bit_index % 8;
    int mask;
    if (from_low_to_high) {
        mask = 1 << bit_in_byte;
    } else {
        mask = 1 << (7 - bit_in_byte);
    }

    return (data[byte_index] & mask) ? 1 : 0;
}

void set_bit(std::vector<uint8_t> &result, int bit_index, uint8_t value, bool from_low_to_high) {
    int byte_index = bit_index / 8;
    int bit_in_byte = bit_index % 8;
    int mask;
    if (from_low_to_high) {
        mask = 1 << bit_in_byte;
    } else {
        mask = 1 << (7 - bit_in_byte);
    }

    if (value == 1) {
        result[byte_index] |= mask;
    } else {
        result[byte_index] &= ~mask;
    }
}

std::vector<uint8_t> permute_bits(std::vector<uint8_t> &data, std::vector<int> p_block, bool from_low_to_high, int start_index) {
    size_t total_bits = data.size() * 8;
    std::vector<uint8_t> result(data.size(), 0);
    int source_index;
    uint8_t bit_value;
    for (int i = 0; i < total_bits; i++) {
        source_index = p_block[i] - start_index;
        bit_value = get_bit(data, source_index, from_low_to_high);
        set_bit(result, i, bit_value, from_low_to_high);
    }

    return result;

}


int main() {
    std::vector<uint8_t> data = {0b10110010};
    std::vector<int> p_block = {7, 6, 5, 4, 3, 2, 1, 0};
    bool from_low_to_high = true;
    int start_index = 0;
    std::vector<uint8_t> result;
    result = permute_bits(data, p_block, from_low_to_high, start_index);
    std::cout << static_cast<int>(data[0]) << " " << static_cast<int>(result[0]) << std::endl;
}
