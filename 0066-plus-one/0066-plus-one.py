class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #FIRST APPROACH
        
        # Converting integer list to string list
        # and joining the list using join()
        #converting integer to srtig and then to list
        #res=int("".join(map(str, digits)))
        #res=res+1
        #final_list = list(map(int, str(res)))
        #return final_list  
    
       #SECOND APPROACH
        
        digits=digits[::-1]
        carry,index=1,0
        
        while carry:
            if index <len(digits):
                if digits[index]==9:
                    digits[index]=0
                else:
                    digits[index]+=1
                    carry=0
            else:
                digits.append(1)
                carry=0
            index+=1
        return digits[::-1]
        