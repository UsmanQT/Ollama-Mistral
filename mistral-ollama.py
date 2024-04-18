import json
import requests
from constants import comments

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "mistral:instruct"  # TODO: update this for whatever model you wish to use


def chat(messages):
    context = []
    for msg in messages:
        r = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": model, "messages": context + [msg], "stream": True},
        )
        r.raise_for_status()
        output = ""

        for line in r.iter_lines():
            body = json.loads(line)
            if "error" in body:
                raise Exception(body["error"])
            if body.get("done") is False:
                message = body.get("message", "")
                content = message.get("content", "")
                output += content
                # the response streams one token at a time, print that as we receive it
                print(content, end="", flush=True)

            if body.get("done", False):
                message["content"] = output
                context.append(message)
                print("\n\n")


def main():
    comments_list = comments.split('\n')  # Split the multiline comments into a list of individual comments
    comments_string = '\n'.join(comments_list) 
    messages = [
        {"role": "user", "content": "Act as a writing professor. You have given a document to be reviewed and commented upon by your students. You collect all the comments made by a student and try to find the general theme of the comments made. The themes are very general and not specific to any document such as references not added, not having more visual information etc. Do you understand your role?"},
        {"role": "user","content": f"Okay. I will start with giving you a list of comments. Your job is to find the general theme from these comments:\n1. {comments_string}"},
        {"role": "user", "content": "Remove any duplicate themes from the output and give exact list of themes"},
    ]

    chat(messages)


if __name__ == "__main__":
    main()
