
def main():
    # This is version # 1
    ver = "This is version of programm # 1"
    
    a = int(input(f"Input a >> "))
    b = int(input(f"Input b >> "))
    print(f"sum = {sum(a, b)}")
    
    return f"{ver}"


def sum(a, b: int) ->int:
    return a + b

if __name__ == "__main__":
    print(main())