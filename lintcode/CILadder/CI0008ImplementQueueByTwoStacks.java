public class Queue {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public Queue() {
        // do initialization if necessary
        stack1 = new Stack<Integer>();
        stack2 = new Stack<Integer>();
    }

    public void push(int element) {
        // move stack2 to stack1, then push to the top of the stack
        Integer entry;
        while (!stack2.empty()) {
            entry = stack2.pop();
            stack1.push(entry);
        }

        stack1.push(new Integer(element));
        while (!stack1.empty()) {
            entry = stack1.pop();
            stack2.push(entry);
        }
    }

    public int pop() {
        return stack2.pop().intValue();
    }

    public int top() {
        return stack2.peek().intValue();
    }
}
