class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        list_of_substrings = self.all_substrings(s)

        answer = self.calc_length(list_of_substrings)

        return answer

    def all_substrings(self, s):

        all_substrings = []

        for letter_counter in range(len(s)):
            memo = []

            for letter_index in range(letter_counter,len(s)):
                letter = s[letter_index]
                if letter not in memo:
                    memo.append(letter)
                else:
                    substring = ''.join(memo)
                    all_substrings.append(substring)
                    break
            
            substring = ''.join(memo)
            all_substrings.append(substring)

        return all_substrings
    
    def calc_length(self, list):

        length = 0

        for substring in list:
            if len(substring) > length:
                length = len(substring)

        return length

if __name__ == '__main__':
    # s = "abcabcbb"
    s = '  '

    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))