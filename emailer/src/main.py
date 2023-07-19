import argparse
from emailer import Emailer, EmailerCreds

DEFAULT_CREDS_FILE = "C:\\Users\\zackb\\emailer_creds\\creds.txt"

def main():

    parser = argparse.ArgumentParser(description='emailer program')
    parser.add_argument('--text', '-t', help='the text to send')
    parser.add_argument('--recipient', '-r', help='the address to send to')
    parser.add_argument('--creds', '-c', help='the creds file')
    args = parser.parse_args()

    if args.creds:
        creds = EmailerCreds(args.creds)
    else:
        creds = EmailerCreds(DEFAULT_CREDS_FILE)

    emailer = Emailer(creds)
    emailer.send_text(args.recipient, args.text)

if __name__ == '__main__':
    main()
