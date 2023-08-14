class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # 누적 합을 저장할 딕셔너리. {누적합 % k: 인덱스}
        d = {0: -1}  # 시작부터의 합이 k의 배수인 경우를 위해 초기값 설정
        acc = 0  # 누적 합 변수
        for i, num in enumerate(nums):
            acc += num
            if k != 0:  # 0으로 나누는 것을 피하기 위해
                acc %= k
            # 만약 이전에 동일한 누적 합 모듈러 k 값을 보았다면,
            # 그 인덱스와 현재 인덱스 사이에 합이 k의 배수인 부분 배열이 존재
            if acc in d:
                if i - d[acc] > 1:  # 부분 배열의 길이가 최소 2 이상인지 확인
                    return True
            else:
                d[acc] = i  # 처음 본 누적 합이면 딕셔너리에 추가

        return False
