class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if parent >= 0 and self.heap[parent].priority < self.heap[index].priority:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        max_task = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_task

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0

