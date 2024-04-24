import google.generativeai as genai

def send_to_gemini(text):
    genai.configure(api_key="YOUR API KEY")

    generation_config = {
      "temperature": 0.9,
      "top_p": 1,
      "top_k": 1,
      "max_output_tokens": 2048,
    }

    safety_settings = [
      # Safety settings
    ]

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config=generation_config,
                                  safety_settings=safety_settings)

    if model:
        convo = model.start_chat(history=[])
        if convo:
            convo.send_message(text)
            return convo.last.text if convo.last else "No response from Gemini."
        else:
            return "Gemini conversation not initialized."
    else:
        return "Gemini model not initialized."
