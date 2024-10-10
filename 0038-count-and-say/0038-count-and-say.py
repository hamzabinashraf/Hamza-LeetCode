class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"  # Initialize the first term
        for iteration in range(n - 1):  # Repeat n - 1 times to get the nth term
            result = ""  # Initialize an empty string for the current term
            count = 1    # Initialize count for the current digit
            digit = prev[0]  # Initialize digit as the first character of the previous term
            # Iterate through the previous term starting from the second character
            for i in range(1, len(prev)):
                # If the current character is the same as the previous one
                if prev[i] == digit:
                    count += 1  # Increment count
                else:
                    # If the current character is different, add the count and digit to the result
                    result += str(count) + digit
                    count = 1  # Reset count for the new digit
                    digit = prev[i]  # Update digit
            # Add the count and digit for the last group of characters
            result += str(count) + digit
            prev = result  # Update prev for the next iteration
        
        return prev  # Return the nth term