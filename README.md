This is a simple generator for enumerating data types in UNION SELECT NULL,NULL -- based SQLi attacks.
I've tried to find a way of doing this through Burp's intruder, but could not figure it out. So I've just wrote this simple script to do it for me.

---

# Usage
1 - Download the `generator.py` script

2 - Navigate to the directory where you've downloaded it to

3 - `python3 generator.py`

4 - `How many positions` - This defines, how many positions will be generated. If you choose 3, the output will be as follows:
`'a',NULL,NULL
NULL,'a',NULL
NULL,NULL,'a'`

5 - `Character(s) to substitute` - This defines what will be substituted instead of the `NULL` character. 

6 - `How many substitutions:` - How many substitutions will be used per line. If you use 2 for example, the output will look like this:
`'a','a',NULL
'a',NULL,'a'
NULL,'a','a'`

![gen](https://github.com/user-attachments/assets/ca4be39e-d72f-46f3-b581-72d23057b837)


