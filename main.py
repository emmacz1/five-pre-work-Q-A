# Question 1
def hello_name(user_name):
    print(f"hello_{user_name}!")

hello_name("John")


# Question 2
def first_odds():
    for i in range(1, 101, 2):
        print(i)

first_odds()


# Question 3
def max_num_in_list(a_list):
    return max(a_list)

numbers = [10, 20, 30, 40, 50]
print("Max number in the list:", max_num_in_list(numbers))


# Question 4
def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False
    
year = 2024
print("Is", year, "a leap year?", is_leap_year(year))


# Question 5
def is_consecutive(a_list):
    return all(a_list[i] == a_list[i-1] + 1 for i in range(1, len(a_list)))

consecutive_list = [2, 3, 4, 5, 6, 7]
non_consecutive_list = [1, 2, 4, 5]
print("Are all numbers consecutive?", is_consecutive(consecutive_list))
print("Are all numbers consecutive?", is_consecutive(non_consecutive_list))