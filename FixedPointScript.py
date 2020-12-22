from fxpmath import Fxp

inputs = input('sign, integers, fractional:').split(', ')
sign = bool(inputs[0])
integers = int(inputs[1])
fractional = int(inputs[2])

words = integers + fractional + sign
#x = (Fxp(number, bool(sign), words, fractional))
#print(x.bin(frac_dot=True))

while True:
    number = float(input('Enter a signed Decimal value to convert:'))
    x = (Fxp(number, sign, words, fractional))
    print(x.bin(frac_dot=True))
    print(x.hex())