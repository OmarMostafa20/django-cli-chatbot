from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class FlanT5Chatbot:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

    # Modify the get_response method in chatbot.py to include a context-enhanced prompt
    def get_response(self, input_text):
        # Enhancing the Prompt
        enhanced_prompt = f"Please provide supportive and clear guidance. The user has asked: '{input_text}'. Your response should be empathetic and informative."

        # Encode the enhanced_prompt
        input_ids = self.tokenizer.encode(enhanced_prompt, return_tensors="pt")

        # Generate a response
        output_ids = self.model.generate(
            input_ids, max_length=100, num_return_sequences=1
        )

        # Decode the response
        response = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return response
