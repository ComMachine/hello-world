class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    public int fibonacci(int n) {
        int firstSeed = 0;
        int secondSeed = 1;
        int result = 0;
        if (n == 1) {
            return firstSeed;
        }
        if (n == 2) {
            return secondSeed;
        }
        for (int i = 3; i <= n; i++) {
            result = firstSeed + secondSeed;
            firstSeed = secondSeed;
            secondSeed = result;
        }
        return result;
    }
}
