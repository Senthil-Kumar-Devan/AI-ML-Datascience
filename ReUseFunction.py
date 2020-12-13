### Create Star Pyramid ### 
def StarPyramid(height):
    """Function prints Pyramid as per the height from the user"""
    descending_star_count = 1
    #Loop through the range form 1 to height*2
    for star_count in range (1, int(height)*2):
        
        #Create increasing * pyramid until max height
        if (star_count <= int(height)):
            star_form_pattern = star_count*"*"
            
        #Create decreasing * pyramid
        else:   
            descending_star_count = int(height)*2 - star_count
            star_form_pattern = descending_star_count*"*"

        print(star_form_pattern)
        
        
### Find Maximum of numbers ###        
def maximum(a,b,c):
    """Function returns maximum of three numbers"""
    # Use the Standard function Maximum
    return max(a,b,c)


### Even/ Odd numbers seperator and counter ###
def Even_Odd_Counter_Seperator(number_series):
    """Function returns Even/ Odd number count"""
    
    #Initialize the Even/Odd counter
    even_count = 0
    odd_count = 0
    
    #Loop through the number series
    for numbers in number_series:
        if((numbers%2) == 0):
            even_count = even_count + 1  

        elif ((numbers%2) != 0):
            odd_count = odd_count + 1

    # Use the Standard function Maximum
    return even_count, odd_count


### Find Even number from the Range of Number series ###
def Find_digit_of_number_is_even_number_from_Number_Range(Range_1, Range_2):
    """Find Even number from the Range of Number series"""
    
    #Initialize final Comma Separated list
    Comma_Sep_number = ""
    
    #Loop through the Range provided
    for number in range(Range_1,Range_2):
        #Initialize even flag to true
        even_flag = True
        
        #Loop through each digits in the given Number
        for i in str(number):
            #if Remainder set the even flag to false, break
            if (int(i)%2 != 0):
                even_flag = False
                break
        # Concatenate all digit_of_number is even_number
        if (even_flag):
            Comma_Sep_number = Comma_Sep_number + str(number) + ","
            
    return Comma_Sep_number


### Find dog's age in dog's years ###
def Find_dogs_age_in_dogs_years(Human_age):
    """To find dog's age in dog's years"""
    #Declaration and Initialization
    One_dog_year = 10.5
    rest_dog_year = 4
    first_two_years = One_dog_year * 2
    
    # Calculation
    return first_two_years + ((int(Human_age) - 2) * rest_dog_year)


### Find Prime Number or Not ###
def Find_Prime_or_not(number):
    if number > 1:
        prime_flag = True

        for num in range(2,number):
            if (number%num == 0):
                prime_flag = False
                break
    else:
        prime_flag = False
        
    return prime_flag


### GCD of Two Numbers ###
def GCD(number1, number2):
    if(number2 == 0):
        return number1
    else:
        return GCD(number2,number1%number2)
