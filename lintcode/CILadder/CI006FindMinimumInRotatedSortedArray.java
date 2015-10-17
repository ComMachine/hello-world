public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] num) {
        // binary search
        if (num.length == 0) {
            // raise exception
            return -1;
        }

        int left = 0;
        int right = num.length - 1;
        int temp = 0;

        while (left < right) {
            if (num[left] < num[right]) {
                // move towards smaller direction (like regular case)
                right = (left + right) / 2;
            } else {
                temp = (left + right) / 2;
                // try and if that value is bigger than num[left] then move left
                if (num[left] == num[temp]) {
                    left = right;
                }
                else if (num[left] < num[temp]) {
                    left = temp;
                } else {
                    right = temp;
                }
            }
        }

        return num[left];
    }
}
