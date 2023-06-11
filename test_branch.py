
def main():
    # This is version # 2
    ver = "This is version of programm # 2"
    
    a = int(input(f"Input a >> "))
    b = int(input(f"Input b >> "))
    c = int(input(f"Input c >> "))
    print(f"sum = {sum(a, b, c)}")
    
    return f"{ver}"


def sum(a, b, c: int) ->int:
    return a + b + c

if __name__ == "__main__":
    print(main())