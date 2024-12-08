#include <cstdint>  // For uintptr_t

int main() {
    uintptr_t start = 0x00000000;  // Starting address (usually invalid)
    uintptr_t end = 0x7fffffffffff; // High address limit (example for 64-bit systems)
    
    for (uintptr_t address = start; address < end; address += sizeof(int)) {
        int *ptr = reinterpret_cast<int*>(address);
        
        // Attempt to safely access the address, but this will likely cause crashes
        try {
            int value = *ptr;
            std::cout << "Value at address " << ptr << ": " << value << std::endl;
        } catch (...) {
            std::cout << "Cannot access address: " << ptr << std::endl;
        }
    }

    return 0;
}

