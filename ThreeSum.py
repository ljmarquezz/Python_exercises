def threeSum(nums):
    triples_list = []
    for i in range(0, len(nums)):
        x = nums[i]
        for j in range(i+1, len(nums)):
            y = nums[j]
            for k in range(j+1, len(nums)):
                z = nums[k]
                if z + y + x == 0:
                    triple = sorted([x, y, z])
                    if triple not in triples_list:
                        triples_list.append(triple)
    return triples_list

numbers = [0,0,0]

print(threeSum(numbers))