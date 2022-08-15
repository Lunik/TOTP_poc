# Time based One-Time-Password - Proof of concept

Now that every web service encourage you, more and more, to use [MFA][mfa-wikipedia] to secure your account, one of them is used most than others : [Time-based one-time password or TOTP][totp-wikipedia] generate a unique code of `6` or more numbers to enter just after typing your password.

The server or web app allowing to setup [TOTP][totp-wikipedia] give a [QRCode][qrcode-wikipedia] to scan (or a [Base32][rfc-4648] string) to configure in a [TOTP][totp-wikipedia] generator app like [Microsoft Authenticator][ms-authenticator-site], [Google Authenticator][google-authenticator-site], [Bitwarden][bitwarden-site] or more.

We all use it, but how does it work ? Is it secure ? Is my account secure when using third-party [TOTP][totp-wikipedia] generator ??

**[Read more][totp-article]**

## What is this repository ?

This repository contains an implementation of the TOTP protocol written in Python.

Feel free to use it in any way you want.

## Usage

```python
python3 main.py
```

**Result :**
```python
Enter secret key : pythoniscool
TOTP code : 738435
```

<!-- links -->

[mfa-wikipedia]: https://en.wikipedia.org/wiki/Multi-factor_authentication
[totp-wikipedia]: https://en.wikipedia.org/wiki/Time-based_one-time_password
[qrcode-wikipedia]: https://en.wikipedia.org/wiki/QR_code
[rfc-4648]: https://tools.ietf.org/html/rfc4648
[ms-authenticator-site]: https://www.microsoft.com/en-us/security/mobile-authenticator-app
[google-authenticator-site]: https://support.google.com/accounts/answer/1066447
[bitwarden-site]: https://bitwarden.com
[totp-article]: https://lunik.tiwabbit.fr/blog/articles/understanding-totp.html