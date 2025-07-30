print("Enter your body measurements")

waist = int(input("Size  of your waist in inches: "))
bust = int(input("Size  of your bust in inches: "))
hip = int(input("Size  of your hip in inches: "))

size_chart = int((waist+bust+hip)/3)


if size_chart < 30:
    print("Check for size XS i.e. extra small")
elif size_chart < 35:
    print("Check for size S i.e. small")
elif size_chart < 40:
    print("Check for size M i.e. medium")
elif size_chart < 45:
    print("Check for size L i.e. large")
elif size_chart < 50:
    print("Check for size XL i.e. extra large")
elif size_chart < 55:
    print("Check for size XXL i.e. double XL")
else:
    print("Something feels wrong")

