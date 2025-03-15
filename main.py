from hypercore.hyper_quantum import HyperQuantum
from hypercore.hyper_network import HyperNetwork
from hypercore.hyper_mind import HyperMind

def main():
    print("HyperAI Başlatılıyor...")
    quantum_engine = HyperQuantum()
    circuit = quantum_engine.create_entangled_circuit()
    
    network = HyperNetwork()
    network.add_node("node_alpha")
    network.secure_upload("node_alpha", "quantum_data", circuit)
    
    ai = HyperMind()
    training_result = ai.train_model()
    print(training_result)

if __name__ == "__main__":
    main()
