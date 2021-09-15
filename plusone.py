class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        len1 = len(digits)
        number = ''.join(map(str, digits))
        number_int = int(number)
        ans = number_int+1
        answer = ''.join(str(ans))
        result = [int(x) for x in str(answer)]
        return result