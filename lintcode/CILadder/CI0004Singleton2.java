class Solution {
    /**
     * @return: The same instance of this class every time
     */
    private static final Solution myInstance = new Solution() ; // class load initialization
    private Solution() {};
    public static Solution getInstance() { // no sychronized needed
        return myInstance;
    }
};
