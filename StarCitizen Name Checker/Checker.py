import requests
import colorama
import concurrent.futures
import os

colorama.init()
cls = lambda: os.system('cls')

with open('words.txt', 'r') as f:
    words = f.read().split()

def make_request(url):
    response = requests.get(url)
    return response.status_code

print ('\033[95m' + ".▄▄ · ▄▄▄▄▄ ▄▄▄· ▄▄▄  ▄▄▄▄▄▄• ▄▌▄▄▄  ▄▄▄▄·       ")
print ("▐█ ▀. •██  ▐█ ▀█ ▀▄ █·•██  █▪██▌▀▄ █·▐█ ▀█▪▪     ")
print ("▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▐▀▀▄  ▐█.▪█▌▐█▌▐▀▀▄ ▐█▀▀█▄ ▄█▀▄ ")
print ("▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█•█▌ ▐█▌·▐█▄█▌▐█•█▌██▄▪▐█▐█▌.▐▌")
print (" ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀ .▀  ▀·▀▀▀▀  ▀█▄▀▪")
print ("                   MX#3145\n")


num_threads = int(input("\033[0m" + "How many threads do you want to use?: "))

with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    results = [executor.submit(make_request, f"https://robertsspaceindustries.com/citizens/{word}") for word in words]

    error_words = []

    for result in concurrent.futures.as_completed(results):
        word = words[results.index(result)]
        status_code = result.result()

        if status_code == 404:
            print(f"\033[92m{word}\033[0m")
            error_words.append(word)
        else:
            print(f"\033[91m{word}\033[0m")

colorama.deinit()

cls()
print("Names that are possibly available:\n")
for word in error_words:
    print(f"\033[92m{word}\033[0m")

input("\nPress Enter to close")
