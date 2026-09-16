class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked: set[int] = set ()
        for num in nums :
            if num in checked:
                return True
            checked.add(num)
        return False