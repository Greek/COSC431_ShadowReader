# `/etc/shadow` reader

Reads the `/etc/shadow` file. That's it.

## Usage

1. (optional) Change the file path in `script.py`

```diff
- SHADOW_PATH = "./shadow.txt"
+ SHADOW_PATH = "/etc/shadow"
```

2. Run the script.

```sh 
$ python3 script.py

User dummy4's password was last changed on 2024-09-25.
User dummy5's password was last changed on 2024-09-25.
User dummy6's password was last changed on 2024-09-25.
User dummy7's password was last changed on 2024-09-25.
User dummy8's password was last changed on 2024-09-25.
User dummy9's password was last changed on 2024-09-25.
User dummy10's password was last changed on 2024-09-25.
User dummy11's password was last changed on 2024-09-25.
User dummy12's password was last changed on 2024-09-25.
User dummy13's password was last changed on 2024-09-25.
User dummy14's password was last changed on 2024-09-25.
User dummy15's password was last changed on 2024-09-25.
User dummy16's password was last changed on 2024-09-25.
User dummy17's password was last changed on 2024-09-25.
User dummy18's password was last changed on 2024-09-25.
User dummy19's password was last changed on 2024-09-25.
User dummy20's password was last changed on 2024-09-25.
User dummy-manual's password was last changed on 2024-09-30.
User dummy21's password was last changed on 2024-09-25.
User dummy22's password was last changed on 2024-09-25.
User tester0's password was last changed on 2024-09-30.
```