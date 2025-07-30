public class StringFunctions {
    public static boolean isPalindrome(String s) {
        return s.equals(new StringBuilder(s).reverse().toString());
    }

    public static int countVowels(String s) {
        String vowels = "aeiouAEIOU";
        int count = 0;
        for (char c : s.toCharArray()) {
            if (vowels.indexOf(c) != -1) {
                count++;
            }
        }
        return count;
    }

    public static String removeDuplicates(String s) {
        StringBuilder result = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (result.indexOf(String.valueOf(c)) == -1) {
                result.append(c);
            }
        }
        return result.toString();
    }

    public static void main(String[] args) {
        String text = "level";
        System.out.println("Is palindrome: " + isPalindrome(text));
        System.out.println("Vowel count: " + countVowels(text));
        System.out.println("Without duplicates: " + removeDuplicates(text));
    }
}
