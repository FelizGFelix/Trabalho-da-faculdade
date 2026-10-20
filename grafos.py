class HeapMax():
    def __init__(self):
        self.nos = 0
        self.heap = []

    def adicionar_no(self, valor):
        self.heap.append(valor)
        self.nos += 1

        f = self.nos

        while True:
            if f == 1:
                break

            p = f // 2
            if self.heap[p-1] >= self.heap[f-1]:
                break
            else:
                self.heap[p-1], self.heap[f-1] = self.heap[f-1], self.heap[p-1]

                f = p

    def mostrar_no(self):
        print(self.heap)

h = HeapMax()
h.adicionar_no()