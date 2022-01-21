import itertools
# from typing_extensions import final
def accountperm():
    s = '0123456789'
    nums = list(s)
    permutations = list(itertools.permutations(nums))
    finallist = ([''.join(permutation) for permutation in permutations])
    return finallist