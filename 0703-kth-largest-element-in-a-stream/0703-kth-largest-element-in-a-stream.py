import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        # If the size of the heap is greater than k, pop out the smallest element
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # The smallest element in the heap is the kth largest element in the list
        return self.heap[0]
