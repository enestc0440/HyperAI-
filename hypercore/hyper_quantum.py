from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator

class HyperQuantum:
    def __init__(self, num_qubits=3):
        self.num_qubits = num_qubits
        self.backend = Aer.get_backend('qasm_simulator')

    def create_entangled_circuit(self):
        qc = QuantumCircuit(self.num_qubits)
        qc.h(0)
        for qubit in range(1, self.num_qubits):
            qc.cx(0, qubit)
        qc.measure_all()
        return qc
