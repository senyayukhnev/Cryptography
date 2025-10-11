#include <iostream>
#include "vector"
#include <cstdint>
#include "cmath"
#include "set"
#include "algorithm"

bool check_p_block(std::vector<int> p_block, int start_index){
    std::set<int> numbers;
    numbers.insert(p_block.begin(), p_block.end());
    std::vector<int> numbers_as_vec(numbers.begin(), numbers.end());
    std::sort(numbers_as_vec.begin(), numbers_as_vec.end());
    std::sort(p_block.begin(), p_block.end());
    if(numbers_as_vec == p_block){
        return true;
    } else{
        return false;
    }
}

uint8_t get_bit(std::vector<uint8_t> &data, int bit_index, bool from_low_to_high) {
    int byte_index = bit_index / 8;
    int bit_in_byte = bit_index % 8;
    int mask;
    if (from_low_to_high) {
        mask = 1 << bit_in_byte;
    } else {
        mask = 1 << (7 - bit_in_byte);
    }

    return (data.at(byte_index) & mask) ? 1 : 0;
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
        result.at(byte_index) |= mask;
    } else {
        result.at(byte_index) &= ~mask;
    }
}

std::vector<uint8_t>
permute_bits(std::vector<uint8_t> &data, std::vector<int> p_block, bool from_low_to_high, int start_index) {
    size_t total_bits = data.size() * 8;
    std::vector<uint8_t> result(data.size(), 0);
    int source_index;
    uint8_t bit_value;
    if (total_bits != p_block.size()) {
        throw std::out_of_range(std::string("P_block doesnt fit with data"));
    }
    if (start_index != 0 && start_index != 1) {
        throw std::invalid_argument("Incorrect start index");
    }
    for (int i = 0; i < total_bits; i++) {
        source_index = p_block.at(i) - start_index;
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
    try {
        result = permute_bits(data, p_block, from_low_to_high, start_index);
    } catch (std::out_of_range &e) {
        std::cerr << "Error: " << e.what() << std::endl;

    } catch (std::invalid_argument &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }
    if(check_p_block(p_block, start_index)){
        std::cout << "P_block is filled" << std::endl;
    } else{
        std::cout << "P_block is incorrect" << std::endl;
    }
    std::cout << "Example data(1 byte): " << static_cast<int>(data[0]) << "\nPermuted data: " << static_cast<int>(result[0]) << std::endl;
}
