import re

def main():
    # great place to learn regex: https://www.computerhope.com/jargon/r/regex.htm
    old_string = "hello kendra, you are a bad ass bitch. Syd loves you so much"

    # Matches any characters between 'a' and 'z'
    new_string = re.sub('a[a-z][a-z]', 'a$$', old_string)

    print(old_string)
    print(new_string)

    old_string = "Winnie is an amazing little puppy and I love her 123 much"

    # Matches anything not contained in brackets
    new_string = re.sub('[^a-zA-z ]', 'sooooo', old_string)

    print(old_string)
    print(new_string)

    old_string = 'I am lost in Paris... this is not fun'

    # Matching any word that starts with a capital
    new_string = re.findall('[A-Z]\w+', old_string)[0]

    print(old_string)
    print(new_string)

if __name__ == "__main__":
    main()