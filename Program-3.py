def generate_series(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:  
            series.append(i)
    return series


a = int(input("Enter a number: "))


if a % 2 == 0:
    a -= 1


result = generate_series(a)
print(", ".join(map(str, result)))
