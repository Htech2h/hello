def find_duplicates(nums):

    duplicates = []
    seen = set()

    for num in nums:
        if num in seen:
            duplicates.append(num)

        else:
            seen.add(num)
    return duplicates

x = [1,2,3,4,5,3,6,7,2]
print(find_duplicates(x))
