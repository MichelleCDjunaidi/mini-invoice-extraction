# loading qwen
from transformers import AutoTokenizer, AutoModelForCausalLM
from data import train_data, test_data

MODEL = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL)

def build_prompt(invoice):
    examples = ""

    for item in train_data:
        examples += f"""
            Invoice:
            {item["text"]}

            Extracted information:
            {item["expected"]}

        """

    return f"""
                You are an invoice information extraction system.

                Extract the following fields:
                - vendor
                - invoice_number
                - total
                - currency

                Here are some examples:

                {examples}

                Now extract the information from this invoice:

                {invoice["text"]}

                Return ONLY a JSON object with these four fields.
            """

def extract_invoice(invoice):
    prompt = build_prompt(invoice)

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(text, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.1
    )

    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    return response.strip()

for invoice in test_data:
    result = extract_invoice(invoice)

    print("=" * 50)
    print("INVOICE:")
    print(invoice["text"])
    print("\nMODEL OUTPUT:")
    print(result)
    print("\nEXPECTED:")
    print(invoice["expected"])