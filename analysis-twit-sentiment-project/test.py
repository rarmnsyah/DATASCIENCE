def number_1(n):
    n = str(n)
    listn = [*n]
    output = ''

    for i in listn:
        output += str(int(i) + 2)[-1]

    return output

def number_1_2(n):
    for i in range(3, -1, -1):
        print(((n // 10**i) + 2) % 10, end = '')    
        n = n % 10**i

def number_2(n):
    output = 'even number' if n % 2 == 0 else 'odd number'
    return output

def number_3(bananas, apples):
    b_price = .99
    a_price = 1.89

    return (bananas*b_price + apples*a_price)*.97



print(number_1(5696))
print(number_1_2(5696))
print(number_2(15))
print(number_3(2, 3.5))
