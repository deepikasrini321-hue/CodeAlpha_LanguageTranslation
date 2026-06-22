import gradio as gr
from deep_translator import GoogleTranslator

# Language dictionary
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Japanese": "ja",
    "Korean": "ko",
    "Chinese": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru"
}

def translate(text, source, target):
    if text.strip() == "":
        return "⚠ Please enter some text."

    try:
        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        return translated

    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(
            lines=5,
            placeholder="Type your text here...",
            label="Enter Text"
        ),
        gr.Dropdown(
            choices=list(languages.keys()),
            value="English",
            label="Source Language"
        ),
        gr.Dropdown(
            choices=list(languages.keys()),
            value="Tamil",
            label="Target Language"
        )
    ],
    outputs=gr.Textbox(label="Translated Text"),

    title="🌍 AI Language Translation Tool",

    description="""
Translate text instantly into multiple languages using Artificial Intelligence.
Developed by Deepika for the CodeAlpha AI Internship.
""",

    theme="soft"
)

demo.launch()