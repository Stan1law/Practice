public class RecursiveFunctions {
    public static int factorial(int n) {
        if (n == 0 || n == 1)
            return 1;
        return n * factorial(n - 1);
    }

    public static int sumDigits(int n) {
        if (n == 0)
            return 0;
        return n % 10 + sumDigits(n / 10);
    }

    public static int fibonacci(int n) {
        if (n <= 1)
            return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    public static void main(String[] args) {
        System.out.println(factorial(5));      // Output: 120
        System.out.println(sumDigits(1234));   // Output: 10
        System.out.println(fibonacci(6));      // Output: 8
    }
}
