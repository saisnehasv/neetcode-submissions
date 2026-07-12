class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operators = ['+','-','*','/']

        for i in tokens:
            if i in operators:
                num1 = numbers.pop()
                num2 = numbers.pop()
                match i:
                    case '+': 
                        numbers.append(num1+num2)
                    case '-':
                        numbers.append(num2-num1)
                    case '*':
                        numbers.append(num1*num2)
                    case '/':
                        numbers.append(int(num2/num1))
            else:
                numbers.append(int(i))
        
        return numbers.pop()







        