from exa_py import Exa

print("Welcome to the Maverick search engine!")
print("This search engine is powered by the Exa API")
print("Learn more about Exa at: https://exa.com")

exa = Exa('YOUR_EXA_API_KEY')

query = input("What would you like to search for?: ")
search = int(input("How many results do you want: "))
mode = input("What mode would you like to use for this search? (search, crawling, answer): ")

if mode == 'search':
    search = exa.search(
        query,
        num_results=search,
        type='auto'
    )
elif mode == 'crawling':
    url = input("What URL would you like to crawl?: ")
    crawl = exa.get_contents(
        [url],
        text = True,
        livecrawl = "always"
    )
elif mode == 'answer':
    model = input("What model would you like to use for this search? (exa or exa-pro): ")
    answer = exa.stream_answer(
        query,
        model=model
    )

BOLD = "\033[1m"
END = "\033[0m"

if mode == 'crawling':
    print(f"\n{BOLD}✨ Crawling Results ✨{END}\n")
    print("─" * 60)
    print(crawl)
    print("─" * 60)
elif mode == 'answer':
    print(f"\n{BOLD}✨ Answer ✨{END}\n")
    print("─" * 60)
    print(f"User: {query}")
    print(f"Exa: {answer}")
    print("─" * 60)
elif mode == 'search':
    print(f"\n{BOLD}✨ Search Results ✨{END}\n")
    print("─" * 60)
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    BOLD = "\033[1m"
    END = "\033[0m"

    print("─" * 60)

    for i, result in enumerate(search.results, 1):
        print(f"{BOLD}{i}.{END} {BLUE}{result.title}{END}")
        print(f"   {GREEN}{result.url}{END}")
        print("─" * 60)

    print(f"\nFound {len(search.results)} results\n")
else:
    print("Invalid mode selected. Please try again.")
