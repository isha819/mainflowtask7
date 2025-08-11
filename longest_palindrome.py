def longest_palindrome(s):
    start = 0
    end = 0

    for i in range(len(s)):
        # Odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1
            r += 1
        
        # Even length
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > end - start:
                start, end = l, r
            l -= 1
            r += 1

    return s[start:end+1]

s = input("Enter string: ")
print("Longest Palindromic Substring:", longest_palindrome(s))
