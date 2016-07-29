#smallest number with 5 cubic permutations.

def smallVersionOfNum(num):
    return "".join(sorted(str(num)))

nums = {}
for num in range(100, 10000):
    cube = num*num*num
    smallCube = smallVersionOfNum(cube)
    if smallCube not in nums:
        nums[smallCube] = [cube]
    else:
        nums[smallCube].append(cube)

    output = nums[smallCube]
    if len(output)==5:
        print cube , num, output[0], smallVersionOfNum(5027*5027*5027)
