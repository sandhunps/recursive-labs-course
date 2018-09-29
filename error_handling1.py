def  a42divideby(divideby):
    try:
        return 42/(divideby)
    except:
        print('error.u tried to divide by zero')
print(a42divideby(21))
print(a42divideby(2))
print(a42divideby(0))
print(a42divideby(1))
