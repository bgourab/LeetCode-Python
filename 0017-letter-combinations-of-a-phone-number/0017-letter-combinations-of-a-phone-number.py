class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap={"2":["a","b","c"],
                "3":["d","e","f"],
                "4":["g","h","i"],
                "5":["j","k","l"],
                "6":["m","n","o"],
                "7":["p","q","r","s"],
                "8":["t","u","v"],
                "9":["w","x","y","z"]}
        
        res=[]
        if not digits:
            return res
        
        
        def backtrack(digits,cur_idx,cur_res):
            if cur_idx >= len(digits):
                res.append("".join(cur_res))
                return
            else:
                for c in numMap[digits[cur_idx]]:
                    cur_res.append(c)
                    backtrack(digits,cur_idx+1,cur_res)
                    cur_res.pop()
        backtrack(digits,0,[])
        return res