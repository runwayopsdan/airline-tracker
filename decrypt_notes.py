def xor_decrypt_hex(hex_str: str, key: str) -> str:
    data = bytes.fromhex(hex_str.strip())
    k = key.encode("utf-8")
    out = bytes([b ^ k[i % len(k)] for i, b in enumerate(data)])
    return out.decode("utf-8", errors="replace")

def main():
    print("=== notes.txt decryptor ===")
    hex_str = input("Paste hex ciphertext: ").strip()
    key = input("Key: ").strip()
    print("\n--- plaintext ---")
    print(xor_decrypt_hex(hex_str, key))

if __name__ == "__main__":
    main()
