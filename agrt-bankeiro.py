# Problema do Banqueiro
def banker_algorithm():
    import numpy as np

    def is_safe_state(available, max_demand, allocation):
        num_processes, num_resources = max_demand.shape
        work = available.copy()
        finish = [False] * num_processes

        while True:
            found = False
            for i in range(num_processes):
                if not finish[i] and all(max_demand[i] - allocation[i] <= work):
                    work += allocation[i]
                    finish[i] = True
                    found = True
            if not found:
                break

        return all(finish)

    available = np.array([3, 3, 2])
    max_demand = np.array([[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]])
    allocation = np.array([[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]])

    print("Estado seguro:" if is_safe_state(available, max_demand, allocation) else "Estado inseguro")
