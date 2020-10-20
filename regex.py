import re

def main():
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

if __name__ == "__main__":
    main()