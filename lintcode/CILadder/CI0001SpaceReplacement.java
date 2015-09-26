public class Solution {
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    public int replaceBlank(char[] string, int length) {
        int numBlank = 0;
        int newLength = length;

        for (int i = 0; i < length; i++) {
            if (string[i] == ' ') {
                numBlank++;
            }
        }

        if (numBlank == 0) {
            return length;
        }

        // otherwise, move the string towards thd end
        newLength = length + numBlank * 2;

        int j;
        int p;
        for (j = length - 1, p = newLength - 1; j >= 0; j--, p--) {
            if (string[j] != ' ') {
                string[p] = string[j];
            } else {
                string[p] = '0';
                p--;
                string[p] = '2';
                p--;
                string[p] = '%';
            }
        }

        return newLength;

    }
}
