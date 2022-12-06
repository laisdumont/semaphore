import semaphore
import sequential


if __name__=="__main__":
    data_concurrent = semaphore.concurrent()
    data_sequential = sequential.sequential()

    print("\n\n------------- CONCORRENTE ----------------")
    print("Duração: {0}s".format(data_concurrent[0]))
    print("Movimentos por segundo: {0}".format(data_concurrent[1]))
    print("------------------------------------------")

    print("\n-------------- SEQUENCIAL ----------------")
    print("Duração: {0}s".format(data_sequential[0]))
    print("Movimentos por segundo: {0}".format(data_sequential[1]))
    print("------------------------------------------\n")

    efficiency = data_sequential[1] - data_concurrent[1]

    if efficiency > 0:
        sequential_per_concurrent = data_sequential[1]/data_concurrent[1]
        print("O modelo sequencial é {0:.3f} mais eficiente que o concorrente.\n".format(sequential_per_concurrent))
    else:
        concurrent_per_sequential = data_concurrent[1]/data_sequential[1]
        print("O modelo concorrente é {0:.3f} mais eficiente que o sequencial.\n".format(concurrent_per_sequential))