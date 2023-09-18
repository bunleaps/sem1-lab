# Sandbox Test
def sandbox():
    x = [2, 2.0, 3, 3.0, 4, 4.0]
     
    for i in x:
        a = i ** 2
        float_a = i ** 2.0
        b = i * i

        print(a, float_a)
        print(b, "\n")


# Calculate suggested snowboard length based on height
def q1():
    print("Enter your height")
    feet = int(input("Feet: "))
    inches = int(input("Inches: "))
    
    cm_per_inch = 2.54
    suggested = 0.88 * (cm_per_inch * ((feet * 12) + inches))
    
    print(f"Suggested board length: {suggested}")
    
    
# Calculate acceleration using mass and force
def q2():
    question = input('Enter the mass in kg and the force in N: ')
    data = question.split(', ')
    
    result = float(data[1]) / float(data[0])
    print(f"The acceleration is {result}")
    
    # alternative way: 
    # mass, force = input('Enter the mass in kg and the force in N: ').split(', ')
    # result = float(force) / float(mass)  
    
    
# Run main program
if __name__ == "__main__":
    sandbox()
