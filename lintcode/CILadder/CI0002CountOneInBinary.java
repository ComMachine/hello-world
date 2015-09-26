public class Solution {
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    public int countOnes(int num) {
        // And with the prepared mask; if non-zero then count+1
        int count = 0;
        int mask = 0x1;
        for (int i = 0; i < 32; i++) {
            if ((num & mask) != 0) {
                count++;
            }
            mask = mask << 1;
        }
        return count;
    }
};
