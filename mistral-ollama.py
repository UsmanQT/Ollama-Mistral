import subprocess
import json


def generate_response(prompt):
    curl_command = f"""curl -s http://localhost:11434/api/generate -d '{{
        "model": "mistral", 
        "stream": false,
        "prompt": "{prompt}",
        "num_ctx": 32768
    }}'"""


    
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    full_response = ""


    while True:
        output_line = process.stdout.readline()
        if not output_line and process.poll() is not None:
            break
        if output_line:
            try:
                response_data = json.loads(output_line.strip())
                full_response += response_data.get("response", "")
            except json.JSONDecodeError:
                return "Invalid response format", 500


    return full_response


def get_user_input_and_generate(comments):
    
    prompt = f"Act as a writing professor. You have given a document to be reviewed and commented upon by your students. You collect all the comments made by a student and try to find the general theme of the comments made. The themes are very general and not specific to any document such as references not added, not having more visual information etc. Okay. I will start with giving you a list of comments. Your job is to find the general theme from these comments: {comments}"
    response = generate_response(prompt)
    print("Response:", response)

if __name__ == '__main__':

    comments = ["This document lacks proper citations. This is a nice article. I loved it."]
    
    comments_str = "\n".join(comments)
    get_user_input_and_generate(comments_str)
