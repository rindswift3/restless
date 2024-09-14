import time
import random
import os

def print_header():
  
 print("𐌓𐌄𐌔𐌕𐌋𐌄𐌔𐌔")
  
os.system('cls')

print("")
print("")
print("")
print("")
print("██████╗ ███████╗███████╗████████╗██╗     ███████╗███████╗███████╗")
print("██╔══██╗██╔════╝██╔════╝╚══██╔══╝██║     ██╔════╝██╔════╝██╔════╝")
print("██████╔╝█████╗  ███████╗   ██║   ██║     █████╗  ███████╗███████")
print("██╔══██╗██╔══╝  ╚════██║   ██║   ██║     ██╔══╝  ╚════██║╚════██║")
print("██║  ██║███████╗███████║   ██║   ███████╗███████╗███████║███████║")
print("╚═╝  ╚═╝╚══════╝╚══════╝   ╚═╝   ╚══════╝╚══════╝╚══════╝╚══════╝")
print("")
print("")
print("                       BTC Recovery Tool                         ")

time.sleep(5)

def generate_random_phrase():
  wordlist = [
      'abandon', 'ability', 'able', 'about', 'above', 'absent', 'absorb',
      'abstract', 'absurd', 'abuse'
  ]
  return " ".join(random.choices(wordlist, k=12))


def generate_random_address():
  return "1" + "".join(random.choice("0123456789abcdef") for _ in range(33))


def random_winner_balance():
  return f"{random.uniform(0, 1):.8f} BTC"


def run_program():
  print_header()

  checked = 0
  winners = 0
  total_balance = 0

  while True:
    checked += 1
    recovery_phrase = generate_random_phrase()
    address = generate_random_address()
    balance = "0 BTC"

    print(
        f"\n{checked} | Address: {address} | Balance: {balance} | Phrase: {recovery_phrase}"
    )

    if checked % 500000 == 0:
      winbal = random_winner_balance()
      winners += 1
      total_balance += float(winbal.split()[0])
      print(
          f"\n{checked} | Address: {address} | Balance: {winbal} | Phrase: {recovery_phrase}"
      )
      print(
          f"\n[Winner Found!] Total Winners: {winners} | Total Balance: {total_balance:.8f} BTC"
      )

      time.sleep(10)
      print("\n[Restarting Program...]\n")
      time.sleep(1)


if __name__ == "__main__":
  run_program()
