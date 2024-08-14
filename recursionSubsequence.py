arr = [1,2,3,4]
def f(ind, nums,arr, n):
    if(ind == n):
        print(nums)
        return 
    # include a new index
    
    nums.append(arr[ind])
    f(ind+1, nums, arr, n)
    nums.pop()
    f(ind+1, nums, arr, n)

print(f(0, [], arr, len(arr)))