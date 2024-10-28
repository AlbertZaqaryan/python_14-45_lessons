# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# nums1[m:m + n] = nums2[:n]
# nums1.sort()
# print(nums1)

# nums = [3, 2, 2, 3]
# val = 3
# while val in nums:
#     nums.remove(val)
# print(nums)

# nums = [0,0,1,1,1,1,1,1,1,2,2,3,3,4]
# print(list(set(nums)))
# for i in nums.copy():
#     if nums.count(i) > 1:
#         nums.remove(i)
# print(nums)


# nums = [2,2,3,3,2,5,3,5,5,5,5,5,5]
# # [2, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# nums.sort()
# print(nums[len(nums) // 2])


# s = "Hello World"
# print(len(s.split(' ')[-1]))

# nums = [2,11,15,7]
# target = 9
# for i in nums:
#     if target - i in nums:
#         print([nums.index(i), nums.index(target - i)])
#         break

# strs = ["flower","flow","flight"]
# strs.sort(key=len)
# index = 1
# while index < len(strs):
#     if strs[0] == strs[index][:len(strs[0])]:
#         index += 1
#     else:
#         strs[0] = strs[0][:-1]
# print(strs[0])