import subprocess
import os
import logging
from datetime import datetime

def setup_logging():
    """Set up logging configuration."""
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    logging.basicConfig(
        filename=os.path.join(log_dir, 'hashcat_log.log'),
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
    )

def run_hashcat(hash_file, wordlist_file, hash_mode, attack_mode):
    """
    Automate the running of Hashcat with given parameters and log progress.
    """
    command = [
        'hashcat',
        '-m', str(hash_mode),
        '-a', str(attack_mode),
        hash_file,
        wordlist_file
    ]
    try:
        logging.info(f"Running Hashcat with command: {' '.join(command)}")
        subprocess.run(command, check=True)
        logging.info("Hashcat run successful.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running Hashcat: {e}")

if __name__ == "__main__":
    setup_logging()

    hash_file = os.path.join('hash_data', 'hashes.txt')
    wordlist_file = os.path.join('hash_data', 'wordlist.txt')

    # Example: Cracking MD5 hashes with dictionary attack
    hash_mode = 0   # MD5
    attack_mode = 0 # Dictionary attack

    logging.info("Starting Hashcat...")
    run_hashcat(hash_file, wordlist_file, hash_mode, attack_mode)
