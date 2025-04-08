from exa_py import Exa
from numpy import c_
from openai import OpenAI
import markdown
import re
import sys
import requests
import json
import os
import shutil
import time


BOLD = "\033[1m"
END = "\033[0m"
CLAUDE_PURPLE = "\033[38;5;134m"
CLAUDE_LAVENDER = "\033[38;5;147m"
CLAUDE_PINK = "\033[38;5;219m"
CLAUDE_BLUE = "\033[38;5;75m"
CLAUDE_CYAN = "\033[38;5;80m"
CLAUDE_WHITE = "\033[38;5;255m"
CLAUDE_BLACK = "\033[38;5;16m"
CLAUDE_BG = "\033[48;5;134m"
CLAUDE_HIGHLIGHT = "\033[48;5;219m\033[38;5;16m"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def animated_print(line, width, color=CLAUDE_PURPLE, delay=0.002):
    for char in line.center(width):
        sys.stdout.write(f"{color}{BOLD}{char}{END}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_header():
    width = shutil.get_terminal_size().columns

    ascii_lines = [
        "███╗   ███╗ █████╗ ██╗   ██╗███████╗██████╗ ██╗ ██████╗██╗  ██╗",
        "████╗ ████║██╔══██╗██║   ██║██╔════╝██╔══██╗██║██╔════╝██║ ██╔╝",
        "██╔████╔██║███████║██║   ██║█████╗  ██████╔╝██║██║     █████╔╝ ",
        "██║╚██╔╝██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗██║██║     ██╔═██╗ ",
        "██║ ╚═╝ ██║██║  ██║ ╚████╔╝ ███████╗██║  ██║██║╚██████╗██║  ██╗",
        "╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝",
        "                                                               ",
        "███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗               ",
        "██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║               ",
        "███████╗█████╗  ███████║██████╔╝██║     ███████║               ",
        "╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║               ",
        "███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║               ",
        "╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝               "
    ]

    for line in ascii_lines:
        animated_print(line, width)

    print()
    print(f"{CLAUDE_WHITE}{'Open-source AI-Powered search engine by Aayan Mishra'.center(width)}{END}")
    print(f"{CLAUDE_CYAN}{'Powered by Exa Search ➤ https://exa.ai'.center(width)}{END}")
    print()



def render_markdown(text):
    html = markdown.markdown(text)

    html = re.sub(r'<strong>(.*?)</strong>', f'{BOLD}\\1{END}', html)
    html = re.sub(r'<h1>(.*?)</h1>', f'\n{BOLD}{CLAUDE_PINK}# \\1{END}\n', html)
    html = re.sub(r'<h2>(.*?)</h2>', f'\n{BOLD}{CLAUDE_PINK}## \\1{END}\n', html)
    html = re.sub(r'<h3>(.*?)</h3>', f'\n{BOLD}{CLAUDE_PINK}### \\1{END}\n', html)
    html = re.sub(r'<li>(.*?)</li>', f'  • \\1', html)
    html = re.sub(r'<a.*?href="(.*?)".*?>(.*?)</a>', f'{CLAUDE_BLUE}\\2{END} [{CLAUDE_LAVENDER}\\1{END}]', html)
    html = re.sub(r'<pre><code>(.*?)</code></pre>', f'{CLAUDE_CYAN}\\1{END}', html, flags=re.DOTALL)
    html = re.sub(r'<code>(.*?)</code>', f'{CLAUDE_CYAN}\\1{END}', html)

    html = re.sub(r'<.*?>', '', html)

    return html

def process_ollama_response(response_text):
    return response_text.strip()

def main():
    clear_screen()
    print_header()

    exa = Exa('YOUR_EXA_API_KEY')

    query = input(f"{BOLD}{CLAUDE_CYAN}What would you like to search for?:{END} ")
    search_count = int(input(f"{BOLD}{CLAUDE_CYAN}How many results do you want:{END} "))

    print(f"\n{BOLD}{CLAUDE_PINK}Available modes:{END}")
    print(f"  {CLAUDE_PURPLE}• search{END}    - Search for information")
    print(f"  {CLAUDE_PURPLE}• crawling{END}  - Crawl a specific URL")
    print(f"  {CLAUDE_PURPLE}• answer{END}    - Get an answer directly from Exa\n")

    mode = input(f"{BOLD}{CLAUDE_CYAN}Select a mode (search/crawling/answer):{END} ").lower()

    if mode == 'search':
        search = exa.search(
            query,
            num_results=search_count,
            type='auto'
        )
    elif mode == 'crawling':
        url = input(f"{BOLD}{CLAUDE_CYAN}What URL would you like to crawl?:{END} ")
        crawl = exa.get_contents(
            [url],
            text = True,
            livecrawl = "always"
        )
    elif mode == 'answer':
        model = input(f"{BOLD}{CLAUDE_CYAN}What model would you like to use? (exa/exa-pro):{END} ").lower()
        answer = exa.stream_answer(
            query,
            model=model
        )
    else:
        print(f"\n{CLAUDE_HIGHLIGHT}❌ Invalid mode selected. Please try again.{END}")
        return

    if mode == 'crawling':
        print(f"\n{BOLD}{CLAUDE_PINK}✨ Crawling Results ✨{END}\n")
        print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")
        print(crawl)
        print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")
    elif mode == 'answer':
        print(f"\n{BOLD}{CLAUDE_PINK}✨ Answer ✨{END}\n")
        print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")
        print(f"{BOLD}User:{END} {query}")
        print(f"{BOLD}Exa:{END} {answer}")
        print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")
    elif mode == 'search':
        print(f"\n{BOLD}{CLAUDE_PINK}✨ Search Results ✨{END}\n")
        print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")

        for i, result in enumerate(search.results, 1):
            print(f"{BOLD}{i}.{END} {CLAUDE_BLUE}{result.title}{END}")
            print(f"   {CLAUDE_LAVENDER}{result.url}{END}")
            print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")

        print(f"\n{CLAUDE_CYAN}Found {len(search.results)} results{END}\n")
        extended = input(f"{BOLD}{CLAUDE_CYAN}Would you like to use an LLM to extend the search? (yes/no):{END} ").lower()

        if extended == "yes":
            print(f"\n{BOLD}{CLAUDE_PINK}Select LLM option:{END}")
            print(f"  {CLAUDE_PURPLE}• local{END}   - Use Ollama for local inference")
            print(f"  {CLAUDE_PURPLE}• api{END}     - Use OpenRouter API\n")

            model = input(f"{BOLD}{CLAUDE_CYAN}Choose an option (local/api):{END} ").lower()

            if model == "local":
                try:
                    ollama_models = requests.get("http://localhost:11434/api/tags").json()
                    print(f"\n{BOLD}{CLAUDE_PINK}Available Ollama models:{END}")
                    for i, model_info in enumerate(ollama_models['models'], 1):
                        print(f"  {CLAUDE_PURPLE}{i}.{END} {model_info['name']}")

                    model_choice = input(f"\n{BOLD}{CLAUDE_CYAN}Enter model name:{END} ")

                    contextllm = search.results
                    system_prompt = f"You are a helpful assistant that provides detailed and accurate information based on the given search results. Here are the results: {contextllm}"

                    print(f"\n{BOLD}{CLAUDE_PINK}✨ Starting conversation with Ollama ({model_choice}) ✨{END}")
                    print(f"Type '{CLAUDE_HIGHLIGHT}exit{END}' to end the conversation.\n")
                    print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")

                    while True:
                        user_input = input(f"{BOLD}You:{END} ")
                        if user_input.lower() == 'exit':
                            break

                        try:
                            response = requests.post(
                                "http://localhost:11434/api/chat",
                                json={
                                    "model": model_choice,
                                    "messages": [
                                        {"role": "system", "content": system_prompt},
                                        {"role": "user", "content": user_input}
                                    ],
                                    "stream": False
                                }
                            )

                            if response.status_code == 200:
                                assistant_response = response.json()["message"]["content"]
                                rendered_response = render_markdown(assistant_response)
                                print(f"{BOLD}Assistant:{END}\n{rendered_response}\n")
                            else:
                                print(f"{CLAUDE_HIGHLIGHT}Error:{END} Failed to get response from Ollama\n")

                        except Exception as e:
                            print(f"{CLAUDE_HIGHLIGHT}Error:{END} {str(e)}\n")
                            print(f"{CLAUDE_PINK}Make sure Ollama is running on your machine.{END}")
                            break

                except Exception as e:
                    print(f"\n{CLAUDE_HIGHLIGHT}⚠️ Ollama connection failed{END}")
                    print(f"{CLAUDE_PINK}⚠️ Make sure Ollama is installed and running{END}")
                    print(f"{CLAUDE_PINK}⚠️ Install Ollama from: https://ollama.com{END}")
                    print(f"{CLAUDE_PINK}⚠️ Falling back to API option...{END}\n")
                    model = "api"

            if model == "api":
                MODEL_ID = input(f"{BOLD}{CLAUDE_CYAN}Enter the model ID e.g deepseek-ai/DeepSeek-R1:{END} ")
                CUSTOM = input(f"{BOLD}{CLAUDE_CYAN}Would you like to use a custom URL? (yes/no):{END} ").lower()
                if CUSTOM == "yes":
                    BASE_URL = input(f"{BOLD}{CLAUDE_CYAN}Enter the custom URL:{END} ")
                else:
                    BASE_URL = "https://openrouter.ai/api/v1"
                API_KEY = input(f"{BOLD}{CLAUDE_CYAN}Enter your API key:{END} ")

                client = OpenAI(
                    base_url=BASE_URL,
                    api_key=API_KEY,
                )

                contextllm = search.results

                messages = [
                    {
                        "role": "system",
                        "content": f"You are a helpful assistant that provides detailed and accurate information based on the given search results. Here are the results: {contextllm}"
                    }
                ]

                print(f"\n{BOLD}{CLAUDE_PINK}✨ Starting conversation with {MODEL_ID} ✨{END}")
                print(f"Type '{CLAUDE_HIGHLIGHT}exit{END}' to end the conversation.\n")
                print(f"{CLAUDE_LAVENDER}{'─' * 60}{END}")

                while True:
                    user_input = input(f"{BOLD}You:{END} ")
                    if user_input.lower() == 'exit':
                        break

                    messages.append({"role": "user", "content": user_input})

                    try:
                        completion = client.chat.completions.create(
                            extra_headers={
                                "HTTP-Referer": "<https://github.com/Aayan-Mishra/Maverick-Search>",
                                "X-Title": "<Maverick Search - Open-source AI-Powerd search engine by Aayan Mishra>",
                            },
                            model=MODEL_ID,
                            messages=messages
                        )

                        assistant_response = completion.choices[0].message.content

                        rendered_response = render_markdown(assistant_response)

                        print(f"{BOLD}Assistant:{END}\n{rendered_response}\n")

                        messages.append({"role": "assistant", "content": assistant_response})

                    except Exception as e:
                        print(f"{CLAUDE_HIGHLIGHT}Error:{END} {str(e)}\n")
                        print(f"{CLAUDE_PINK}Please check your API key and model ID and try again.{END}")

if __name__ == "__main__":
    main()
