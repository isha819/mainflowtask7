def is_palindrome(s):
    return s == s[::-1]

def backtrack(start, path, s, result):
    if start == len(s):
        result.append(path[:])
        return
    for end in range(start+1, len(s)+1):
        if is_palindrome(s[start:end]):
            path.append(s[start:end])
            backtrack(end, path, s, result)
            path.pop()

s = input("Enter string: ")
result = []
backtrack(0, [], s, result)
print("Palindrome partitions:")
for part in result:
    print(part)
