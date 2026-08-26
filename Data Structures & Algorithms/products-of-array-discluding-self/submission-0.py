class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [1]*len(nums)
        arr2 = [1]*len(nums)

        product_so_far = 1

        for i in range(1,len(nums)):
            product_so_far = nums[i-1] * product_so_far
            arr1[i] = product_so_far
        
        product_so_far = 1

        for i in range(len(nums)-2,-1,-1):
            product_so_far = nums[i+1] * product_so_far
            arr2[i] = product_so_far


        for i in range(len(nums)):
            arr1[i] = arr1[i] * arr2[i]

        return arr1