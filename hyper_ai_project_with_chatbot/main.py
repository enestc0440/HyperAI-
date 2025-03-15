from hypercore.hyper_quantum import HyperQuantum
from hypercore.hyper_network import HyperNetwork
from hypercore.hyper_mind import HyperMind
from hypercore.chatbot import SimpleChatbot

def main():
    print("HyperAI Başlatılıyor...")
    quantum_engine = HyperQuantum()
    entanglement_matrix = quantum_engine.create_entangled_circuit()

    network = HyperNetwork()
    network.add_node("node_alpha")
    network.secure_upload("node_alpha", "quantum_data", entanglement_matrix.tolist())

    ai = HyperMind()
    training_result = ai.train_model()
    print(training_result)

    # AI Chatbot başlatılıyor
    chat_loop(ai, network)

def chat_loop(ai, network):
    chatbot = SimpleChatbot()
    print("\n🤖 HyperAI AI Chatbot Başlatıldı! 'exit' yazarak çıkabilirsiniz.")
    
    while True:
        user_input = input("👤 ")
        if user_input.lower() == "exit":
            print("👋 HyperAI kapanıyor...")
            break
        elif "eğitim" in user_input.lower():
            print("📢 AI modeli eğitiliyor...")
            result = ai.train_model()
            print("✅", result)
        elif "ağ durumu" in user_input.lower():
            print("🌐 Ağdaki mevcut düğümler:", list(network.nodes.keys()))
        else:
            print("🤖", chatbot.get_response(user_input))

if __name__ == "__main__":
    main()
