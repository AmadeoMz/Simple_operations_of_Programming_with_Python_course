import sys

#This program reads two numbers from the command-line and does the indicated operation with them
#Usage: $python arith.py (add/subtract/multiply/divide) (number1) (number2)
#Example: 
#$python arith.py add 1 2
# 3.0

def main():
        script = sys.argv[0]
        operation = sys.argv[1]
        nums = sys.argv[2:]
        assert operation in ['add', 'subtract', 'multiply', 'divide'], 'No operation allowed:'+operation
        assert len(nums)==2, 'Please introduce two numbers to operate with'
        math(nums, operation)

def math(nums, operation):
        if operation == 'add':
         value = float(nums[0])+float(nums[1])
        elif operation == 'subtract':
         value = float(nums[0])-float(nums[1])
        elif operation== 'multiply':
         value = float(nums[0])*float(nums[1])
        elif operation == 'divide':
         value = float(nums[0])/float(nums[1])
        print(value)

if __name__ == '__main__':
        main()
