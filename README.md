# LyriBot 🎶 (Work in Progress)

**LyriBot** is an AI-powered Bollywood song generator that transforms **newspaper articles into Bollywood-style lyrics** in Hindi. It uses a **fine-tuned GPT model** trained on Bollywood songs to generate creative, poetic lyrics based on news summaries. 🚀

## 📌 Project Overview
LyriBot is designed to:
1. **Train an AI model on Bollywood song lyrics** 🏆
2. **Take any newspaper article as input** 📰
3. **Summarize the article into a single line** ✍️
4. **Convert the summary into a Hindi Bollywood song** 🎤

## 🚧 Current Progress
✅ **Data Collection & Cleaning**
- Collected **72 Bollywood-style romantic songs** in Hindi.
- Cleaned the dataset while **preserving `===NEW SONG===` separators.**

✅ **Model Setup & Tokenization**
- Selected **`ai-forever/mGPT`** (a multilingual GPT model) for Hindi support.
- Tokenized song lyrics and **prepared them for training.**

✅ **Fine-Tuning Setup**
- Configured **training parameters** (batch size, epochs, logging, etc.).
- Created a **custom dataset** with `input_ids` and `labels` for causal language modeling.

🔄 **Next Steps:**
- **Complete model training** 🎯
- **Test song generation** from news articles 🎶
- **Optimize lyrics quality & melody structure** 🎼
- **Deploy as a Chrome extension or API** 🌐

## 🛠️ How to Run (Work in Progress)
1. Clone the repository (to be added once complete).
2. Install dependencies:
   ```sh
   pip install transformers datasets torch sentencepiece accelerate
   ```
3. Run `model.ipynb` in VS Code or Jupyter Notebook.
4. Train the model and generate Bollywood-style lyrics!

---
🎵 **LyriBot – Bringing Bollywood Lyrics to Life with AI!** 🎤✨

