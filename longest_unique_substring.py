def longest_unique_substring(s):
    max_len = 0
    start = 0
    seen = {}  

    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= start:
            start = seen[s[i]] + 1
        seen[s[i]] = i
        if i - start + 1 > max_len:
            max_len = i - start + 1
    return max_len

def solve_longest_unique_substring():
    s = input("Enter string: ").strip()
    result = longest_unique_substring(s)
    print("Length of longest substring without repeating characters:", result)

if __name__ == "__main__":
    solve_longest_unique_substring()
