import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleChatbot:
    def __init__(self):
        self.knowledge_base = {
            "merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
            "nasılsın": "Ben bir yapay zeka botuyum, duygularım yok ama yardım etmeye hazırım!",
            "sen kimsin": "Ben HyperAI chatbot'um! Sorularınıza yanıt vermek için buradayım.",
            "ne yapıyorsun": "Size yardımcı olmak için buradayım. Bir işlem yapmak ister misiniz?",
            "eğitim başlat": "📢 AI modeli eğitiliyor...",
            "ağ durumu": "🌐 Ağdaki mevcut düğümleri kontrol ediyorum...",
            "şifrele": "🔒 Şifreleme özelliği şu an eklenmedi."
        }
        self.vectorizer = TfidfVectorizer()
        self.fit_vectorizer()

    def fit_vectorizer(self):
        self.vectorizer.fit(self.knowledge_base.keys())

    def get_response(self, user_input):
        inputs = list(self.knowledge_base.keys())
        vectors = self.vectorizer.transform(inputs)
        user_vector = self.vectorizer.transform([user_input])
        similarities = cosine_similarity(user_vector, vectors).flatten()

        best_match_index = similarities.argmax()
        if similarities[best_match_index] > 0.2:  # Benzerlik eşik değeri
            return self.knowledge_base[inputs[best_match_index]]
        return "⚡ Bununla ilgili bir bilgim yok, ancak öğrenebilirim!"

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    while True:
        user_input = input("👤 ")
        if user_input.lower() == "exit":
            print("👋 Chatbot kapanıyor...")
            break
        print("🤖", chatbot.get_response(user_input))
