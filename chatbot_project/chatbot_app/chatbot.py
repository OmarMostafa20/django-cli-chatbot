from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline


class ChatBot:
    def __init__(self):
        self.model_name = "google/flan-t5-base"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    def get_response(self, context):
        # Encode and generate response
        context_ids = self.tokenizer.encode(context, return_tensors="pt")
        output_ids = self.model.generate(
            context_ids,
            max_length=512,
            num_return_sequences=1,
            temperature=0.7,
            do_sample=True,
        )
        response = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return response


class SummaryBot:
    def __init__(self):
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def get_response(self, context):
        response = self.summarizer(
            context, max_length=130, min_length=10, do_sample=False
        )

        return response[0]["summary_text"]
