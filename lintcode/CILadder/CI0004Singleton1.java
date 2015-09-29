class Solution {
    /**
     * @return: The same instance of this class every time
     */
    private static Solution myInstance = null;
    private Solution() {};
    public static synchronized Solution getInstance() { // use synchronized
        if (myInstance == null) {
            myInstance = new Solution();
        }
        return myInstance;
    }
};
