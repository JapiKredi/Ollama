import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

header = {
    "Content-Type": "application/json",
}

def generate_response(prompt):
    data = {
        "model": "mistral",
        "stream": False,
        "prompt": prompt,
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_text = response.text
        data = json.loads(response_text)
        actual_response = data['response']
        print(actual_response)
    else:
        print("Error: ", response.status_code, response.text)
        return None

iface = gr.Interface(
    fn=generate_response,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Enter your Prompt here..."),
    outputs='text'
)

iface.launch()