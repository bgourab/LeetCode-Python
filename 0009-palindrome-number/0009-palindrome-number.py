class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=0
        if (x<0):
            return False
        if (x==0):
            return True
        if (x%10==0):
            return False
        originalNum=x
        reverseNum=0
        while (x>0):
            lastDigit = x%10
            reverseNum= reverseNum*10 + lastDigit
            x = x//10
        return reverseNum == originalNum
            