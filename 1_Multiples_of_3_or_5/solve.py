'''
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

  Find the sum of all the multiples of 3 or 5 below 1000.

'''

def isMultipleOfThree(number):
    digits = [int(d) for d in str(number)];
    return sum(digits) % 3 == 0;

def isMultipleOfFive(number):
    digits = [ int(d) for d in str(number)];
    return (digits[-1] == 5) or (digits[-1] == 0);

def getSumOfThreesAndFives(number):
    sum = 0;
    for i in range(1,number):
        if isMultipleOfThree(i) or isMultipleOfFive(i):
            sum = sum + i;

    return sum;



print(getSumOfThreesAndFives(1000));
