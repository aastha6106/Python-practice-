value = input("Enter a value: ")

try:
    int_value = int(value)
    print(f"The value '{value}' is of type Integer.")
except ValueError:
    try:
        float_value = float(value)
        print(f"The value '{value}' is of type Float.")
    except ValueError:
        try:
            complex_value = complex(value)
            print(f"The value '{value}' is of data type Complex. ")
        except ValueError:
            try:
                bool_value = bool(int(value))
                print(f"The value '{value}' is of type Boolean. ")
            except ValueError:
                try:
                    str_value = str(value)
                    print(f"The value '{value}' is of type string. ")
                except ValueError:
                    print("Unknown data type.")

    
