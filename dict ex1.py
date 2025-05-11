exercise = [
{
    'question' : "How much is 2+2",
    'options'  :  ['2', '3', '4', '6'],
    'result' : '4'
},

{
    'question' : "How much is 10/2",
    'options'  :  ['3','5','4','6'],
    'result' : '5'
},
{
    'question' : "How much is 10*10",
    'options'  :  ['200','150','120','100'],
    'result' : '100'
}
]
number_of_hits = 0
for question in exercise:
    print('Question',question['question'])
    print()

    options = question['options']
    for i,option in  enumerate(options):
     print(i,")",option)
    print()
    user_answer = input("Type your answer = ")

    correct = False
    int_answer = None
    qtd_options = len(options)


    if user_answer.isdigit():
       int_answer = int(user_answer)
    if int_answer is not None:
       if int_answer >= 0 and int_answer < qtd_options:
          if options[int_answer] == question['result']:
             correct = True
             number_of_hits += 1
    
    if correct:
       print('Correct answer')
       print()
    else:
       print("Wrong answer")
       print()
print(f'You got {number_of_hits} out of {len(question)} right')
             