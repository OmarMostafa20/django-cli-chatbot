from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


class ChatBot:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "facebook/blenderbot-400M-distill"
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "facebook/blenderbot-400M-distill"
        )

    def get_response(self, message):
        # Tokenize the input message
        inputs = self.tokenizer([message], return_tensors="pt")

        # Generate a response
        reply_ids = self.model.generate(
            **inputs,
            max_length=1000,
            do_sample=True,  # Enable sampling
            temperature=0.7,  # Control randomness
            top_k=0,  # Optionally control the number of highest probability vocabulary tokens to keep for top-k-filtering
            num_return_sequences=1,  # Number of sequences to generate (you can generate more than one for varied responses)
        )

        # Decode and print the response
        response = self.tokenizer.batch_decode(reply_ids, skip_special_tokens=True)
        return response[0]


class SummaryBot:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def get_response(self, context):
        response = self.summarizer(
            context, max_length=130, min_length=10, do_sample=False
        )

        return response[0]["summary_text"]
