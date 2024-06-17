class Solution {
    public boolean canJump(int[] nums) {
        int arr=0;
        for (int i=0 ; i< nums.length ; i++){
            if(arr<i){
                return false;
            }
            arr= Math.max(arr, i+nums[i]);
        }
        return true ;
    }
}