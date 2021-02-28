

# 19 => nineteen
# 20 => twenty
# 30 => thirty
# 40 => forty

to_english = {
    1: 'one',
    2: 'two', 
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six', 
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand'
}

def letter_count(num):
    if num in to_english.keys():
        # print(num, len(to_english[num]))
        return len(to_english[num])
 
    if num <= 99: # it will also be > 20
        tens = num // 10
        ones = num - tens * 10
        # print(tens, ones)
        # print(num, len(to_english[tens*10]) + len(to_english[ones]))
        return len(to_english[tens*10]) + len(to_english[ones])
    
    if num > 99:
        hundreds = num//100
        rest = num - hundreds*100

        if num % 100 == 0:
            return letter_count(hundreds)+len('hundred')
        else:
            return letter_count(hundreds)+len('hundredand')+letter_count(rest)


# print(letter_count(342))
# print(letter_count(115))

sum(letter_count(i) for i in range(1, 1001))