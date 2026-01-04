# 🚀 PEGASUS Text Summarizer

This project is a **web-based text summarization app** using the **PEGASUS model** (Pre-training with Extracted Gap-sentences for Abstractive Summarization) from Hugging Face.  
It creates **abstractive summaries** from long text inputs with state-of-the-art performance.

### 🛠️ Tools & Technologies Used
- **🐍 Python**
- **🤗 Transformers Library** – Hugging Face
- **🚀 PEGASUS Model** – `google/pegasus-cnn_dailymail`
- **🔍 Regular Expressions (`re` module)** – Clean summaries
- **🎨 Gradio** – Interactive web interface
- **💻 Jupyter / Colab / Kaggle** – Testing environment
- **📊 NLP Evaluation (Optional)** – ROUGE scores for summarization quality

### ⚡ Features
- Clean, readable summaries
- Works well on **small or large datasets**
- Emoji-rich, interactive UI
- Example texts included for quick testing
- Link to [PEGASUS Paper](https://huggingface.co/papers/1912.08777)

### 📦 Installation
```bash
git clone https://github.com/your-username/PEGASUS-Summarizer.git
cd PEGASUS-Summarizer
pip install -r requirements.txt
python app.py
