# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        # 거북이와 토끼 초기화
        slow = head
        fast = head.next

        # 토끼가 연결 리스트의 끝에 도달할 때까지 반복
        while fast is not None and fast.next is not None:
            # 거북이와 토끼가 만나면 사이클이 존재한다는 것이므로 True를 반환
            if slow == fast:
                return True
            
            # 거북이는 한 칸씩, 토끼는 두 칸씩 전진
            slow = slow.next
            fast = fast.next.next
        
        # 토끼가 연결 리스트의 끝에 도달하면 사이클이 없다는 것이므로 False를 반환
        return False
        