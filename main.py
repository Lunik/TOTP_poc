import base64
import hmac
import struct
import time

def hotp(counter, key, digits_count=6):
  bytes_counter = struct.pack('>Q', counter)

  key = key + '=' * ((8 - len(key)) % 8)
  bytes_key = base64.b32decode(key)

  mac = hmac.new(bytes_key, bytes_counter, "SHA1").digest()

  offset = mac[-1] & 0x0F
  dynamic_truncation = mac[offset:offset+4]
  extract_31 = struct.unpack('>L', dynamic_truncation)[0] & 0x7fffffff

  return str(extract_31)[-digits_count:].zfill(digits_count)


def totp(key):
  counter = int(time.time() / 30)

  return hotp(counter, key)


if __name__ == "__main__":
  key = input("Enter secret key : ").upper()

  print("TOTP code :", totp(key))