#pip3 install tqdm
import pyfiglet
import zipfile
from tqdm import tqdm

ascii_banner = pyfiglet.figlet_format("ZipCracker")
print(ascii_banner)

zip_file = "locked.zip"
wordlist = "wordlist.txt"

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
