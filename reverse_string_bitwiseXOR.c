// 344. Reverse String
// https://leetcode.com/problems/reverse-string/description/
// Given a character array s, reverse the array in-place.

// Use bitwise XOR to swap characters without using a temporary variable.
void reverseString(char* s, int sSize) {
    for (int i = 0; i < sSize / 2; i++) {
        // Swap using only `i`, computing the reverse index dynamically
        s[i] = s[i] ^ s[sSize - 1 - i];
        s[sSize - 1 - i] = s[i] ^ s[sSize - 1 - i];
        s[i] = s[i] ^ s[sSize - 1 - i];
    }
}