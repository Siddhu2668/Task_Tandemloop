def generate_series(a):
    series = [i for i in range(1, 2 * a, 2)]  
    return series


a = int(input("Enter a number: "))


result = generate_series(a)
print(", ".join(map(str, result)))
