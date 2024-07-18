
def is_leap(year):
    leap = False

    if (year%4==0):
        if (year%100!=0):
            leap= False
        elif (year%400==0):
            leap=True
    return leap

if __name__ == "__main__":
    year = int(input("Enter a year: "))
    print(is_leap(year))


"""Explanation:
Initial Condition (year % 4 == 0):
If the year is divisible by 4, it might be a leap year.
Nested Condition (year % 100 == 0):
If the year is divisible by 100, it might not be a leap year unless it is also divisible by 400.
Further Nested Condition (year % 400 == 0):
If the year is divisible by 400, it is a leap year.
Else, if it is divisible by 100 but not 400, it is not a leap year.
Else Clause (year % 100 != 0):
If the year is not divisible by 100 but divisible by 4, it is a leap year."""
