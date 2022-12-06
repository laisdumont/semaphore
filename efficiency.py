import semaphore
import sequential

data_concurrent = semaphore.concurrent()
data_sequential = sequential.sequential()

print("\n\nDuração Concorrente: {0}s".format(data_concurrent[0]))
print("Duração Sequencial: {0}s".format(data_sequential[0]))

efficiency = data_concurrent[1] - data_sequential[1]
print("Eficiência: {0}".format(efficiency))
