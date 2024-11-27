# Banker-s-Algorithm
The Banker's Algorithm, introduzido por Edsger Dijkstra, é usado para evitar 
deadlocks em sistemas de alocação de recursos. Ele simula o comportamento de um
banqueiro que decide se um novo pedido de recursos pode ser concedido com segurança.

Funcionamento:

O sistema verifica se os recursos solicitados podem ser alocados sem levar a um estado inseguro.

Um estado é considerado seguro se houver uma sequência em que todos os processos possam concluir suas execuções.

Caso contrário, o pedido de recursos é negado.

Este algoritmo é amplamente usado em sistemas de tempo compartilhado.
