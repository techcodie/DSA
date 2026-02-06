class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, sum, combinations):
            if sum == target:
                result.append(combinations)
                return
            if i >= len(candidates) or sum > target:
                return

            for j in range(target // candidates[i] + 1):
                # decision to use j times of a candidate
                tmp_array = combinations + [candidates[i]] * j
                dfs(i + 1, sum + candidates[i] * j, tmp_array)

        dfs(0, 0, [])
        return result