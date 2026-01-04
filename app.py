import gradio as gr
from transformers import pipeline

summarizer = pipeline("summarization", model="google/pegasus-cnn_dailymail")

def summarize_text(text):
    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
    return summary[0]['summary_text']

iface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=15, placeholder="📝 Enter your text here...", label="Input Text"),
    outputs=gr.Textbox(lines=10, placeholder="Summary will appear here...", label="Summary"),
    title="🚀 PEGASUS Summarizer",
    description="""
    **Summarize long text quickly!** ✨  
    Enter any text and get an **abstractive summary** using the [PEGASUS](https://huggingface.co/papers/1912.08777) model.  
    Works well even for **long paragraphs and articles**. 📰📚
    """
)

if __name__ == "__main__":
    iface.launch(share=True)
