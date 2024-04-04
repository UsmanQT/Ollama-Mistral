# How to run models likst Mistral-7B and Llama using Ollama on M1/M2 Mac?


## Description
This project will show you how to setup with Ollama on Apple MacBooks and also how to run python scripts to call the Mistral or Llama2 using API.

## Installation

### Install Ollama on your Mac

1. Visit this official [Ollama Website](https://ollama.com/blog)
2. Click on the "Download" Button.
3. Once Ollama is downloaded on your mac. Move it to your Applications folder and run it through Spotlight search.
4. Now open the terminal and type 
```
ollama run mistral
```
It will take a few minutes to download and run the mistral model
5. Once the download is done and you see ">>>", start chatting with the mistral model to see if everything is fine.
6. You can also download llama2 model by typing in your terminal
```
ollama run llama2
```
7. Some commands to interact with ollama using terminal
    - To see all the downloaded models: 
        ```
        ollama list
        ```
    - To run a model:
        ```
        ollama run
        ```
    - To delete a model:
        ```
        ollama rmi
        ```

### To run the ollama models using python scripts

Install the project by following these steps: 
1. Clone the repository: 
    ```
    git clone https://github.com/UsmanQT/Ollama-Mistral.git
    ```
2. Navigate to the project directory:
    ```
    cd Ollama-Mistral
    ```
## Usage
To use the project, follow these steps:
1. Run the python script:
    ```
    python3 mistral-ollama.py
    ```
2. Enter prompt: "Hey how are you doing?"

3. You can change the model's name to "llama2" in the curl command if you wish to use llama2.

## Wonderful !! You just ran models from Ollama on your local MacBook

## Contact
For inquiries, please contact:
- Email: usman.nja.14@gmail.com
- LinkedIn: [@iusmanq](https://www.linkedin.com/in/iusmanq/)
