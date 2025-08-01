# Basic string creation and properties.

# 1. Literal definitions
single_quoted = 'Hello, world!'
double_quoted = "Python is awesome"
triple_quoted = """This is
a multi-line
string."""

# 2. Raw strings (e.g. for Windows paths or regex)
raw_path = r"C:\Users\Muhammad"

# 3. Byte string (immutable sequence of bytes)
byte_str = b"byte data"

# 4. f strings (formatted string literals)
name = "Alice"
greeting = f"Hello, {name}!"

print(single_quoted)         # Hello, world!
print(double_quoted) 	     # Python is awesome
print(triple_quoted)         # preserves newlines
print(raw_path)              # C:\Users\Muhammad
print(byte_str)              # b'byte data'
print(byte_str.decode())     # byte data
print(greeting)              # Hello, Alice!
