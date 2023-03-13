def FourSum(nums, target):
    solution_list = []
    if not nums:
        return []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(k+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quadruple = sorted([nums[i], nums[j], nums[k], nums[l]])
                        if quadruple not in solution_list:
                            solution_list.append(quadruple)
    return solution_list

if __name__ == '__main__':
    my_list = [1, 2, 2, 3, 1, 4, 1, 5, 7, 8, 6, 9, 3, 4, 2, 1]
    print (FourSum(my_list, 10))
