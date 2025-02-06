import json
import logging
from scripts.run_hashcat import run_hashcat

def load_hash_types():
    with open('hash_data/hash_types.json', 'r') as f:
        return json.load(f)

def load_attack_modes():
    with open('hashcat_config/attack_modes.json', 'r') as f:
        return json.load(f)

def main():
    logging.info("Loading hash types and attack modes...")
    hash_types = load_hash_types()
    attack_modes = load_attack_modes()

    for hash_type in hash_types:
        for attack_mode in attack_modes:
            logging.info(f"Cracking hashes of type {hash_type} with attack mode {attack_mode}...")
            run_hashcat('hash_data/hashes.txt', 'hash_data/wordlist.txt', hash_type, attack_mode)

if __name__ == "__main__":
    main()
