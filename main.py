def generate_report(amount_of_words, char_amounts):
  sorted_char_amounts = dict(sorted(char_amounts.items(), key=lambda item: item[1], reverse=True))
  print("--- Being report of books/frankenstein.txt ---")
  print(f"{amount_of_words} words found in the document")
  for char in sorted_char_amounts:
    print(f"The '{char}' character was found {char_amounts[char]} times")
  print("--- End of report ---")


def get_char_amounts(text):
  lower_text = list(text.lower())
  char_amounts = {}
  for char in lower_text:
    if char.isalpha() == False:
      continue
    if char in char_amounts:
      char_amounts[char] += 1
    else:
      char_amounts[char] = 1
  return char_amounts

def get_amount_of_words(text):
  return len(text.split())

def main():
  with open("./books/frankenstein.txt") as f:
      text = f.read()
      amount_of_words = get_amount_of_words(text)
      char_amounts = get_char_amounts(text)
      generate_report(amount_of_words, char_amounts)

main()


