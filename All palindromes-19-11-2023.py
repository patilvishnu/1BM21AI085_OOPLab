def palindromeSubStrs(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    distinct_palindromes = set()
 
    for gap in range(n):
        for i in range(n - gap):
            j = i + gap
            if gap == 0:
                dp[i][j] = True
            elif gap == 1:
                dp[i][j] = s[i] == s[j]
            else:
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
 
            if dp[i][j]:
                distinct_palindromes.add(s[i:j + 1])
 
    return distinct_palindromes
 
 

s = "GADAG"
palindromes = palindromeSubStrs(s)
print("No of distinct palindromic substrings are:", len(palindromes))
for palindrome in palindromes:
    print(palindrome)
