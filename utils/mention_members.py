MENTION_MEMBERS = [
    'chaonan.wang@avantcorp.com',
]

if __name__ == "__main__":
    print("[{}]".format(", ".join("'" + member + "'" for member in MENTION_MEMBERS)))